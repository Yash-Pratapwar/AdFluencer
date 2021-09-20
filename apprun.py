from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
# from flask_user import roles_required
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///adfluencer.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
    pswd1 = db.Column(db.String(150))
    pswd2 = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
class user_infl(db.Model, UserMixin):
    __tablename__ = 'user_infl'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150), unique=True)
    acc_handler_name = db.Column(db.String(150))
    acc_handler_desig = db.Column(db.String(150))
    comp_website = db.Column(db.String(150))
    ph_no = db.Column(db.Integer)
    comp_email = db.Column(db.String(150))
    ah_email = db.Column(db.String(150))
    ah_email = db.Column(db.String(150))
    pswd1 = db.Column(db.String(150))
    pswd2 = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
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
        adv_regis = user_advt(company_name=company_name,acc_handler_name=acc_handler_name,acc_handler_desig=acc_handler_desig,
        comp_website=comp_website, ph_no=ph_no, comp_email=comp_email, ah_email=ah_email,pswd1=pswd1,pswd2=pswd2,gender=gender )
        db.session.add(adv_regis)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('advertiser-registration.html')

@app.route('/inf_regis', methods=['GET', 'POST'])
def inf_regis():
    if request.method == 'POST':
        return redirect(url_for('home'))
    else:
        return render_template('influencer-registration.html')

if __name__ == "__main__":
    app.run(debug=True)
