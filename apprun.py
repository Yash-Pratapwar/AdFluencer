from flask import Flask, request, render_template, url_for, redirect, flash
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, login_manager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
# from flask_bcrypt import Bcrypt

# from flask_user import roles_required
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///adfluencer.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'b8f3aabd290888870cc64c5ab34d0484'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


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
    age = db.Column(db.Integer)
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
        user_a = user_advt.query.filter_by(comp_email=email).first()
        user_i = user_infl.query.filter_by(inf_email=email).first()
        if user_a:
            
            if check_password_hash(user_a.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user_a, remember=True)
                return redirect('/advt/dashboard')
            else:
                flash('Incorrect password, try again.', category='error')
        
        elif user_i:
            if check_password_hash(user_i.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user_i, remember=True)
                return redirect('/infl/dashboard')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template('login.html')

@login_manager.user_loader
def load_user(id):
    return user_advt.query.get(int(id)) or user_infl.query.get(int(id))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("logged out successfully!", category='success')
    return redirect(url_for('home'))

@app.route('/advt/dashboard')    # @route() must always be the outer-most decorator
@login_required
def advt_dashboard():
    return render_template('advt_dashboard.html')

@app.route('/infl/dashboard')    # @route() must always be the outer-most decorator
@login_required
def infl_dashboard():
    return render_template('infl_dashboard.html')





@app.route('/infl/portfolio_details')    # @route() must always be the outer-most decorator
@login_required
def portfolio_details():
    return render_template('infl_portfolio.html')

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
                hashed_password = generate_password_hash(pswd1, method='sha256')    
                adv_regis_user = user_advt(company_name=company_name,acc_handler_name=acc_handler_name,
                acc_handler_desig=acc_handler_desig,comp_website=comp_website, ph_no=ph_no, comp_email=comp_email, 
                ah_email=ah_email,password=hashed_password,gender=gender )
                db.session.add(adv_regis_user)
                db.session.commit()
                flash('Account created! Please login', category='success')
                return redirect(url_for('login'))
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
        age = request.form.get("age")
        pswd1 = request.form.get("pswd1")
        pswd2 = request.form.get("pswd2")
        gender = request.form["gender"]
        if (fname == "" or fname == None) :
            flash("First Name cannot be empty", category= "error")
        elif (lname) == "":
            flash("Last Name cannot be empty", category= "error")
        elif (smh) == "":
            flash("Please enter your social media handle URL (in format: https://www.sample.com)", category= "error")
        elif (ph_no) == "":
            flash("Phone Number cannot be empty", category= "error")
        elif (inf_email) == "":
            flash("Influencer's Email Address cannot be empty", category= "error")
        elif (pswd1) == "":
            flash("Password cannot be empty", category= "error")
        elif (pswd2) == "":
            flash("Password cannot be empty", category= "error")
        elif (age) == "":
            flash("Please enter your age", category= "error")
        elif (pswd1 != pswd2):
            flash("Passwords should match", category= "error")
        elif (gender) == "":
            flash("Please Select a Gender", category= "error")
        else:
            user = user_infl.query.filter_by(inf_email=inf_email).first()
            if user:
                flash('Email already exists.', category='error')
                return render_template('influencer-registration.html')
            else:
                hashed_password = generate_password_hash(pswd1, method='sha256')    
                inf_regis_user = user_infl(fname=fname,lname=lname,smh=smh, 
                ph_no=ph_no, inf_email=inf_email, password=hashed_password,age=age, gender=gender )
                db.session.add(inf_regis_user)
                db.session.commit()
                flash('Account created! Please login', category='success')
                return redirect(url_for('login'))
    return render_template('influencer-registration.html')

@app.route('/myprofile')
@login_required
def myprofile():
    return render_template('infl_profile')    


if __name__ == "__main__":
    app.run(debug=True)
