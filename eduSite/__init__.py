from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__, template_folder='html_templates')     #https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
app.config['SECRET KEY'] = '88ef963d5d6c95f2a27d286046f76d6a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from eduSite import routes
