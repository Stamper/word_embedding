from gensim.models import KeyedVectors

from . import celery, db
from .models import Sentence, Task, Result


@celery.task
def calculate_wm_distance(sentence_id):
    sentence = Sentence.query.get(sentence_id)
    if not sentence:
        return

    task = Task.query.filter_by(sentence_id=sentence_id).first()
    if task:
        return

    model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
    new_task = Task(sentence_id=sentence_id)
    db.session.add(new_task)
    db.session.flush()
    target_sentence = sentence.value
    sentences = Sentence.query.filter_by(id != sentence_id).all()
    for s in sentences:
        distance = model.wmdistance(target_sentence, s.value)
        new_result = Result(task_id=new_task.id, sentence_id=s.id, value=distance)
        db.session.add(new_result)

    new_task.completed = True
    db.session.commit()
