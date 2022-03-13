from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))