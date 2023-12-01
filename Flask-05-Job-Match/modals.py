
from app import db

class JobSeeker(db.Model):
    __tablename__ = 'job_seeker'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, default=True)
    skills = db.Column(db.String(255))
    experience = db.Column(db.String(50))
    bio = db.Column(db.Text)
    availability = db.Column(db.Date)
