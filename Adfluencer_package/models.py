from Adfluencer_package import db 
from flask_login import UserMixin 
from datetime import datetime
class user_advt(db.Model, UserMixin):
    __tablename__ = 'user_advt'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150), unique=False)
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
