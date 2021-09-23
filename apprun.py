from flask import Flask, request, render_template, url_for, redirect, flash
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_bcrypt import Bcrypt

# from flask_user import roles_required
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///adfluencer.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'adfluencer@secret'
db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

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
    # pswd2 = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
class user_infl(db.Model, UserMixin):
    __tablename__ = 'user_infl'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150), unique=True)
    lname = db.Column(db.String(150))
    smh = db.Column(db.String(150))
    # ph_no = db.Column(db.String(150))
    ph_no = db.Column(db.Integer)
    inf_email = db.Column(db.String(150))
    password = db.Column(db.String(150))
    # pswd2 = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pswd')
        
        user = user_advt.query.filter_by(comp_email=email).first()
        if user:
            
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return render_template('advt_dashboard.html')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template('login.html')

# @app.route('/advt/dashboard')    # @route() must always be the outer-most decorator
# @login_required
# @roles_required('advt')
# def advt_dashboard():
#     # render the admin dashboard
#     return render_template('advt_dashboard.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/adv_regis', methods=['GET', 'POST'])
def adv_regis():
    if request.method == 'POST':
        company_name = request.form.get("company_name")
        acc_handler_name = request.form.get("acc_handler_name")
        acc_handler_desig = request.form.get("acc_handler_desig")
        comp_website = request.form.get("comp_website")
        ph_no = request.form.get("ph_no")
        comp_email = request.form.get("comp_email")
        ah_email = request.form.get("ah_email")
        pswd1 = request.form.get("pswd1")
        pswd2 = request.form.get("pswd2")
        gender = request.form["gender"]
        if (company_name == "" or company_name == None) :
            flash("Company Name cannot be empty", category= "error")
        elif (acc_handler_name) == "":
            flash("Account Handler Name cannot be empty", category= "error")
        elif (acc_handler_desig) == "":
            flash("Account Handler's Designation cannot be empty", category= "error")
        elif (comp_website) == "":
            flash("Company Website cannot be empty", category= "error")
        elif (ph_no) == "":
            flash("Phone Number cannot be empty", category= "error")
        elif (comp_email) == "":
            flash("Company's Email Address cannot be empty", category= "error")
        elif (ah_email) == "":
            flash("Account Handler's Email cannot be empty", category= "error")
        elif (pswd1) == "":
            flash("Password cannot be empty", category= "error")
        elif (pswd2) == "":
            flash("Password cannot be empty", category= "error")
        elif (gender) == "":
            flash("Please Select a Gender", category= "error")
        else:
            user = user_advt.query.filter_by(comp_email=comp_email).first()
            if user:
                flash('Email already exists.', category='error')
                return render_template('advertiser-registration.html')
            else:
                hashed_password = generate_password_hash(pswd1)    
                adv_regis_user = user_advt(company_name=company_name,acc_handler_name=acc_handler_name,acc_handler_desig=acc_handler_desig,
                comp_website=comp_website, ph_no=ph_no, comp_email=comp_email, ah_email=ah_email,password=hashed_password,gender=gender )
                db.session.add(adv_regis_user)
                db.session.commit()
                return redirect(url_for('home'))
    return render_template('advertiser-registration.html')

@app.route('/inf_regis', methods=['GET', 'POST'])
def inf_regis():
    if request.method == 'POST':
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        smh = request.form.get("smh")
        # comp_website = request.form.get("comp_website")
        ph_no = request.form.get("ph_no")
        inf_email = request.form.get("inf_email")
        # ah_email = request.form.get("ah_email")
        pswd1 = request.form.get("pswd1")
        pswd2 = request.form.get("pswd2")
        gender = request.form["gender"]
        inf_regis_user = user_infl(fname=fname,lname=lname,smh=smh,
        ph_no=ph_no, inf_email=inf_email, pswd1=generate_password_hash(pswd1, method='sha256'), gender=gender )
        db.session.add(inf_regis_user)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('influencer-registration.html')

if __name__ == "__main__":
    app.run(debug=True)
