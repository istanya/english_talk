from app import db

class Video(db.Model):
    __tablename__ = 'video'

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Integer, db.ForeignKey('talks_type.id'))
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)