#database model
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_migrate import Migrate

 


class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False, unique=True)
    password=db.Column(db.String(150))



class Doc(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    phone_no=db.Column(db.String(150), unique=True)
    name=db.Column(db.String(150))
    password=db.Column(db.String(150))

class P_details(db.Model):
    __tablename__="patientDetails"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(150),  nullable=False)
    bld_grp=db.Column(db.String(1), nullable=False)
    height=db.Column(db.String(10), nullable=False)


