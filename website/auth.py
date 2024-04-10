from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route("/login", methods = ['GET', 'POST'])

def login():
  data = request.form
  print(data)
  return render_template("login.html", boolean = True)

@auth.route("/logout")

def logout():
  return "<p>logout</p>"

@auth.route("/sign-up", methods = ['GET', 'POST'])

def sign_up():
  if request.method == 'POST':
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(firstName) < 2: 
      flash('First name most be greater than two characters', category='error')
    if len(lastName) < 2:
      flash('Last name most be greater than two characters', category='error')
    if len(email) < 5:
      flash('Email most be greater than two characters', category='error')
    if password1 != password2:
      flash('Password dont match', category='error')
    if len(password1) < 5:
      flash('Password most be greater than five characters', category='error')
    else:
    #add user to data base
      flash('Account creatly succesfully', category='success')

    



  return render_template('sign_up.html')