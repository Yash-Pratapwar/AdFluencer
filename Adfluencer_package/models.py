from enum import unique
from re import S
from typing import Text

from sqlalchemy.orm import backref
from Adfluencer_package import db
from flask_login import UserMixin 
from datetime import datetime

class users(db.Model, UserMixin):   
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    comp_name = db.Column(db.String(150), unique=False)
    acc_handler_name = db.Column(db.String(150), nullable = True)
    acc_handler_desig = db.Column(db.String(150), nullable = True)
    comp_website = db.Column(db.String(150), nullable = True)
    ph_no = db.Column(db.Integer)
    comp_email = db.Column(db.String(150), nullable = True, unique = True)
    ah_email = db.Column(db.String(150), nullable = True)
    password = db.Column(db.String(150))
    acc_handler_gender = db.Column(db.String(150), nullable = True)    
    fname = db.Column(db.String(150), nullable = True)
    lname = db.Column(db.String(150), nullable = True)
    smh = db.Column(db.String(150), nullable = True)    
    inf_email = db.Column(db.String(150), unique=True)
    age = db.Column(db.Integer, nullable = True)
    gender = db.Column(db.String(150))
    acc_type = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    advts = db.relationship('advertisements', backref='owner') 

class advertisements(db.Model, UserMixin):
    __tablename__ = 'advertisements'
    id  = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comp_name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    desc = db.Column(db.String(1000))
    brand = db.Column(db.String(150))
    deadline = db.Column(db.Integer)
    prdt_sp = db.Column(db.String(1000))
    age_grp = db.Column(db.String(20))
    name = db.Column(db.Text, nullable = False)
    mimetype = db.Column(db.Text, nullable = False)
    date_uploaded = db.Column(db.DateTime, default = datetime.utcnow)
