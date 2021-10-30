from enum import unique
from re import S
from typing import Text

from sqlalchemy.orm import backref
from Adfluencer_package import db 
from flask_login import UserMixin 
from datetime import datetime

class user_advt(db.Model, UserMixin):
    __tablename__ = 'user_advt'
    id = db.Column(db.Integer, primary_key=True)
    comp_name = db.Column(db.String(150), unique=False)
    acc_handler_name = db.Column(db.String(150))
    acc_handler_desig = db.Column(db.String(150))
    comp_website = db.Column(db.String(150))
    ph_no = db.Column(db.Integer)
    comp_email = db.Column(db.String(150))
    ah_email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    acc_handler_gender = db.Column(db.String(150))
    acc_type = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    advts = db.relationship('advertisements', backref='owner') 

class user_infl(db.Model, UserMixin):
    __tablename__ = 'user_infl'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150))
    lname = db.Column(db.String(150))
    smh = db.Column(db.String(150))
    ph_no = db.Column(db.Integer)
    inf_email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(150))
    acc_type = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class advertisements(db.Model, UserMixin):
    __tablename__ = 'advertisements'
    id  = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user_advt.id'))
    comp_name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    desc = db.Column(db.String(1000))
    brand = db.Column(db.String(150))
    deadline = db.Column(db.Integer)
    prdt_sp = db.Column(db.String(1000))
    age_grp = db.Column(db.String(20))
    # prdt_imgs = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable = False)
    mimetype = db.Column(db.Text, nullable = False)
    date_uploaded = db.Column(db.DateTime, default = datetime.utcnow)

    
