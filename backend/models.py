from . import app, db


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    preview = db.Column(db.String(100))
    sentences = db.relationship('Sentence', backref='text', lazy='dynamic')


class Sentence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_id = db.Column(db.Integer, db.ForeignKey('text.id'), nullable=False)
    value = db.Column(db.Text())
    task = db.relationship('Task', backref='sentence', uselist=False)
    result = db.relationship('Result', backref='sentence', uselist=False)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.id'), nullable=False)
    completed = db.Column(db.Boolean(), default=False)
    results = db.relationship('Result', backref='task', lazy='dynamic')


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.id'), nullable=False)
    value = db.Column(db.Float())
