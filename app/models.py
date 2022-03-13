from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    pitches = db.relationship('Pitch', backref = 'user', passive_deletes= True, lazy='dynamic')


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.Text, nullable = False)
    pitch_category = db.Column(db.String(128))
    author = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable = False )
