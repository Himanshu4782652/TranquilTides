from . import db
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    assessments = db.relationship("Assessment", backref="user", lazy=True)


class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anxiety = db.Column(db.Integer, nullable=False)
    depression = db.Column(db.Integer, nullable=False)
    schizophrenia = db.Column(db.Integer, nullable=False)
    bipolar = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String(100), nullable=True)  # ML prediction result
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
