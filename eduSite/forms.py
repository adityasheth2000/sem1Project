from wtforms import Form, StringField, PasswordField, validators, SubmitField, BooleanField
#https://wtforms.readthedocs.io/en/stable/forms.html
#https://wtforms.readthedocs.io/en/stable/validators.html

class signupForm(Form):
    username = StringField('Username', [validators.Length(min=2, max=16)])
    email = StringField('Email Address', [validators.Email()])
    password = PasswordField('Password', [validators.Length(min=5, max=25)])
    confirmPassword = PasswordField('Confirm Password', [validators.EqualTo('password')]) #password mismatch message to be added
    submit = SubmitField('Sign up') #terms of use to be added

class loginForm(Form):
    email = StringField('Email Address', [validators.Email()])
    password = PasswordField('Password', [validators.Length(min=5, max=25)])
    #remember = BooleanField('Keep me logged in')
    submit = SubmitField('Login')
