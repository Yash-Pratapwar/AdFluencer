from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/adv_regis')
def adv_regis():
    return render_template('advertiser-registration.html')

@app.route('/inf_regis')
def inf_regis():
    return render_template('influencer-registration.html')






app.run(debug=True)
