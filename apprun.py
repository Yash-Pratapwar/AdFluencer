from flask import Flask, request, render_template, url_for, redirect, flash, session
from flask_bootstrap import Bootstrap
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, login_manager, login_user, login_required, logout_user, current_user
from sqlalchemy.orm import session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager


# from flask_user import roles_required
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///adfluencer.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'b8f3aabd290888870cc64c5ab34d0484'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# class GreetUserForm(FlaskForm):
#     submit = SubmitField(label=('Submit'))
#     fname = StringField('First Name', id='name', validators=[DataRequired(), Alpha(), Length(
#         min=1), ], render_kw={"placeholder": "Enter Your First Name*"})
#     lname = StringField('Last Name', id='name', validators=[InputRequired(
#         message='username req'), Alpha()], render_kw={"placeholder": "Enter Your Last Name*"})
#     smh = URLField('Social Media Handle', id='name', validators=[DataRequired(
#     ),URL("Enter valid URL")], render_kw={"placeholder": "URL format: https://sample.com*"})
# ph_no = StringField("Phone number:",id='name', validators=[DataRequired(), NumberInput()], render_kw={"placeholder": "Enter Your phone number*"})
# def validate_phone(self, ph_no):
#     try:
#         p = phonenumbers.parse(ph_no.data)
#         if not phonenumbers.is_valid_number(p):
#             raise ValueError()
#     except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
#         raise ValidationError('Invalid phone number')
# def validate_username(self, fname):
#     excluded_chars = " *?!'^+%&/()=}][{$#"
#     for char in self.fname.data:
#         if char in excluded_chars:
#             raise ValidationError(
#                 f"Character {char} is not allowed in username.")
# def validate_image(form, field):
#     if field.data == field.default:
#         return True
#     url_validator = validators.URL()
#     return url_validator(form, field)


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
    return user_infl.query.get(int(id)) or user_advt.query.get(int(id))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("logged out successfully!", category='success')
    return redirect(url_for('home'))


# @route() must always be the outer-most decorator
@app.route('/advt/dashboard')
@login_required
def advt_dashboard():
    return render_template('advt_dashboard.html')


@app.route('/advt/advertise')
@login_required
def advt_advertise():
    return render_template('advt_advertisements.html')


# @route() must always be the outer-most decorator
@app.route('/infl/dashboard')
@login_required
def infl_dashboard():
    name = current_user.fname
    return render_template('infl_dashboard.html', name=name)


# @route() must always be the outer-most decorator
@app.route('/infl/portfolio_details')
@login_required
def portfolio_details():
    return render_template('infl_portfolio.html')


# @route() must always be the outer-most decorator
@app.route('/infl/my_profile')
@login_required
def my_profile():
    return render_template('infl_profile.html')


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
        acc_handler_gender = request.form["gender"]
        acc_type = 'advt'
        # if (company_name == "" or company_name == None):
        #     flash("Company Name cannot be empty", category="error")
        # elif (acc_handler_name) == "":
        #     flash("Account Handler Name cannot be empty", category="error")
        # elif (acc_handler_desig) == "":
        #     flash("Account Handler's Designation cannot be empty", category="error")
        # elif (comp_website) == "":
        #     flash("Company Website cannot be empty", category="error")
        # elif (ph_no) == "":
        #     flash("Phone Number cannot be empty", category="error")
        # elif (comp_email) == "":
        #     flash("Company's Email Address cannot be empty", category="error")
        # elif (ah_email) == "":
        #     flash("Account Handler's Email cannot be empty", category="error")
        # elif (pswd1) == "":
        #     flash("Password cannot be empty", category="error")
        # elif (pswd2) == "":
        #     flash("Password cannot be empty", category="error")
        # elif (gender) == "":
        #     flash("Please Select a Gender", category="error")
        # else:
        user = user_advt.query.filter_by(comp_email=comp_email).first()
        if user:
            flash('Email already exists.', category='error')
            return render_template('advertiser-registration.html')
        else:
            hashed_password = generate_password_hash(
                pswd1, method='sha256')
            adv_regis_user = user_advt(company_name=company_name, acc_handler_name=acc_handler_name,
            acc_handler_desig=acc_handler_desig, comp_website=comp_website, ph_no=ph_no, comp_email=comp_email,
            ah_email=ah_email, password=hashed_password, acc_handler_gender=acc_handler_gender, acc_type=acc_type)
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
        ph_no = request.form.get("ph_no")
        inf_email = request.form.get("inf_email")
        age = request.form.get("age")
        pswd1 = request.form.get("pswd1")
        gender = request.form["gender"]
        acc_type = 'infl'

        user = user_infl.query.filter_by(inf_email=inf_email).first()
        if user:
            flash('Email already exists.', category='error')
            return render_template('influencer-registration.html')
        else:
            hashed_password = generate_password_hash(
                pswd1, method='sha256')
            inf_regis_user = user_infl(fname=fname, lname=lname, smh=smh,ph_no=ph_no, 
            inf_email=inf_email, password=hashed_password, age=age, gender=gender, acc_type=acc_type)
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
