from app import db


class TalksType(db.Model):
    __tablename__ = 'talks_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    image = db.Column(db.Text, nullable=False)
