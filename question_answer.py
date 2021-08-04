from database import db


class QuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    product = db.Column(db.Text)

    def __repr__(self):
        return '<QuestionAnswer %r>' % self.id
