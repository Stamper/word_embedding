from re import split

from flask import request
from sqlalchemy.exc import DatabaseError

from . import app, db
from .models import *
from .tasks import calculate_wm_distance


@app.route('/text', methods=('GET', 'POST'))
def text_endpoint():
    if request.method == 'GET':
        page = request.args.get('page', type=int, default=1)
        texts = Text.query.paginate(page, per_page=10)

        return {
            'status': 'ok',
            'count': Text.query.count(),
            'data': [
                {
                    'id': t.id,
                    'preview': t.preview,
                    'sentences': t.sentences.count()
                } for t in texts.items
            ]
        }

    elif request.method == 'POST':
        try:
            text = request.get_data(as_text=True).strip().replace('\n', '')

        except:
            return {'status': 'error'}

        sentences = split(r'[\.\!\?]', text)

        try:
            new_text = Text(preview=text[:100].strip())
            db.session.add(new_text)
            db.session.flush()

            for s in sentences:
                sentence = s.strip()
                if sentence:
                    new_sentence = Sentence(text_id=new_text.id, value=sentence)
                    db.session.add(new_sentence)

            Task.query.delete()
            Result.query.delete()
            db.session.commit()
            return {'status': 'ok', 'id': new_text.id}

        except DatabaseError:
            return {'status': 'error'}


@app.route('/text/<int:text_id>', methods=('GET',))
def get_text(text_id):
    text = Text.query.get_or_404(text_id)

    return {
        'status': 'ok',
        'data': [
            {
                'id': s.id,
                'value': s.value
            } for s in text.sentences
        ]
    }

@app.route('/sentence/<int:sentence_id>', methods=('GET',))
def sentence_endpoint(sentence_id):
    pending = True
    sentence = Sentence.query.get_or_404(sentence_id)

    task = Task.query.filter_by(sentence_id=sentence_id).first()
    if task:
        pending = not task.completed

    else:
        calculate_wm_distance.delay(sentence_id)

    if pending:
        return {'status': 'pending'}

    else:
        return {
            'status': 'ok',
            'data': [
                {
                    'id': r.id,
                    'sentence_id': r.sentence_id,
                    'text_id': r.sentence.text_id,
                    'value': r.sentence.value,
                    'distance': r.value
                } for r in sentence.task.results.order_by(Result.value).limit(100)
            ]
        }