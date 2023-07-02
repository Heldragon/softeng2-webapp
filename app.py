from flask import Flask, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField,validators
from pyzbar.pyzbar import decode
from PIL import Image

app = Flask(__name__)

class RegistrationForm(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    firstname = StringField('First Name', [validators.DataRequired(), validators.Length(min=4, max=25)])
    lastname = StringField('Last Name', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.DataRequired(), validators.Length(min=6, max=55)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route("/")
def index():
  return render_template('home.html')

@app.route("/loginpage", methods=['GET', 'POST'])
def login():
  return render_template('loginpage.html')

@app.route("/signuppage", methods=['GET', 'POST'])
def signup():
  form = RegistrationForm()

  if form.validate():
     return '<h1>' + form.username.data + '</h1>'
  
  return render_template('signup_form.html', form=form)

@app.route("/pricechecker")
def pricechecker():
  return render_template('pricecheckerpage.html')

@app.route("/yourcart")
def cartpage():
  return render_template('cartpage.html')

@app.route('/scan', methods=['POST'])
def scan():
    file = request.files['file']
    image = Image.open(file.stream)
    results = decode(image)
    barcode_data = results[0].data.decode('utf-8')
    return barcode_data

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)