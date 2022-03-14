from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    pitches = db.relationship('Pitch', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref='user',
                               passive_deletes=True)
    likes = db.relationship('Like', backref='user',
                            passive_deletes=True)


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch = db.Column(db.Text, nullable=False)
    pitch_category = db.Column(db.String(128))
    author = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    comments = db.relationship(
        'Comment', backref='pitch', passive_deletes=True)
    likes = db.relationship('Like', backref='pitch', passive_deletes=True)


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(200), nullable=False)
    comment_author = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    comment_pitch = db.Column(db.Integer, db.ForeignKey(
        'pitches.id', ondelete='CASCADE'), nullable=False)


class Like(db.Model):

    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    like_author = db.Column(db.Integer, db.ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    like_pitch = db.Column(db.Integer, db.ForeignKey(
        'pitches.id', ondelete='CASCADE'), nullable=False)
