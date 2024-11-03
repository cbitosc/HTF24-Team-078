#database model
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_migrate import Migrate

 


class Patient(db.Model, UserMixin):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False, unique=True)
    password=db.Column(db.String(150))




class Doc(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    phone_no=db.Column(db.String(150), unique=True)
    name=db.Column(db.String(150))
    password=db.Column(db.String(150))

class P_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    fname = db.Column(db.String(100), nullable=False)
    first=db.Column(db.Boolean, default=True)
    email= db.Column(db.String(100))
    age = db.Column(db.String(10), nullable=False)
    gender= db.String(db.String(10))
    bld_grp=db.Column(db.String(5), nullable=False)
    existing=db.Column(db.String(1000))
    allergies= db.Column(db.String(1000))

    height=db.Column(db.String(10), nullable=True)


