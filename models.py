from flask_login import UserMixin
from app import db
from sqlalchemy import *

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    keydir = db.Column(db.String(100000000000000000000))
    download = db.Column(db.String(100))
    otp = db.Column(db.Integer)
    verified = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime)