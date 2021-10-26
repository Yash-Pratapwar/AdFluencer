from flask import Blueprint, app
# from Adfluencer_package import views
from flask import request, render_template, url_for, redirect, flash, session
from flask_login import login_manager, login_user, login_required, logout_user, current_user
from flask import render_template, request
from Adfluencer_package.models import user_advt, user_infl
from werkzeug.security import generate_password_hash, check_password_hash
from Adfluencer_package import db


views = Blueprint('views', __name__)



@views.route('/')
def home():
    return render_template('index.html')


@views.route('/login', methods=['GET', 'POST'])
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





@views.route('/logout')
@login_required
def logout():
    logout_user()
    flash("logged out successfully!", category='success')
    return redirect(url_for('views.home'))


# @route() must always be the outer-most decorator
@views.route('/advt/dashboard')
@login_required
def advt_dashboard():
    return render_template('advt_dashboard.html')


@views.route('/advt/advertise')
@login_required
def advt_advertise():
    return render_template('advt_advertisements.html')


# @route() must always be the outer-most decorator
@views.route('/infl/dashboard')
@login_required
def infl_dashboard():
    name = current_user.fname
    return render_template('infl_dashboard.html', name=name)


# @route() must always be the outer-most decorator
@views.route('/infl/portfolio_details')
@login_required
def portfolio_details():
    return render_template('infl_portfolio.html')


# @route() must always be the outer-most decorator
@views.route('/infl/my_profile')
@login_required
def my_profile():
    return render_template('infl_profile.html')


@views.route('/register')
def register():
    return render_template('registration.html')


@views.route('/adv_regis', methods=['GET', 'POST'])
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
            return redirect(url_for('views.login'))
    return render_template('advertiser-registration.html')


@views.route('/inf_regis', methods=['GET', 'POST'])
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
            return redirect(url_for('views.login'))
    return render_template('influencer-registration.html')


@views.route('/myprofile')
@login_required
def myprofile():
    return render_template('infl_profile')