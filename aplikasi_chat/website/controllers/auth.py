from flask import Blueprint, render_template, request, redirect, url_for
from website.models.user import User
from website import argon2
from flask_login import login_user,login_required,logout_user,current_user
import uuid


auth = Blueprint('auth',__name__)

@auth.route('/')
def home():
    return render_template('homepage.html')

@auth.route('/login',methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
     # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password':
        # Create variables for easy access
        id = uuid.uuid1()
        username = request.form['username']
        password = request.form['password']
        # Create User object
        user = User.query.filter_by(username=username).first()
        # If account exists show error and validation checks
        if user:
            if(argon2.check_password_hash(user.password, password)):
                # Create session data, we can access this data in other routes
                login_user(user, remember=True)
                # Redirect to user page
                return redirect(url_for('users.home'))
            else:
                # wrong password
                msg = 'Wrong Password'
        else:
            # Account doesnt exist or username incorrect
            msg = "Username Incorrect/Doesn't Exist"
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('login.html', msg=msg)

@auth.route('/register',methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'no_hp' in request.form and 'tanggal_lahir' in request.form:
        # Create variables for easy access
        id = uuid.uuid1()
        username = request.form['username']
        password = argon2.generate_password_hash(request.form['password'])
        no_hp = request.form['no_hp']
        tanggal_lahir = request.form['tanggal_lahir']
        # Create User object
        user = User.query.filter_by(username=username,no_hp=no_hp,tanggal_lahir=tanggal_lahir).first()
        # If account exists show error and validation checks
        if user:
            msg = 'Account already exists!'
        else:
            new_user = User(id=id,username=username,password=password,no_hp=no_hp,tanggal_lahir=tanggal_lahir)
            new_user.create()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))