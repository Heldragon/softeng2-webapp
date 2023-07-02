from flask import Flask, render_template, request
from pyzbar.pyzbar import decode
from PIL import Image

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('home.html')

@app.route("/loginpage")
def login():
  return render_template('loginpage.html')

@app.route("/signuppage")
def signup():
  return render_template('signup_form.html')

@app.route("/pricechecker")
def pricechecker():
  return render_template('pricecheckerpage.html')

@app.route("/yourcart")
def cartpage():
  return render_template('cartpage.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)