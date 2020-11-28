from app import db


class StartPhrases(db.Model):
    __tablename__ = 'start_phrases'

    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.Text, nullable=False)
