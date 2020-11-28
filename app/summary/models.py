from app import db

class Retelling(db.Model):
    __tablename__ = 'retelling'

    id = db.Column(db.Integer, primary_key=True)
    talks_type_id = db.Column(db.Integer, db.ForeignKey('talks_type.id'))
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)