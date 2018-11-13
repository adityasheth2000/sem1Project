from flask import render_template
from eduSite import app
from eduSite.forms import signupForm, loginForm
#from eduSite.models import User, Post

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = signupForm()
    return render_template('signup.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    return render_template('login.html', form=form)
