from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')








app.run(debug=True)
