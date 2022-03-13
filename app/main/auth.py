from flask import Blueprint, render_template, flash, redirect, url_for, request
from werkzeug.security import  generate_password_hash, check_password_hash
from .forms import Signup, Login
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login = Login()

    if login.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = request.form.get('remember')

        email_exist = User.query.filter_by(email = email).first()

        if email_exist:
            if check_password_hash(User.password, password):
                flash(f'You have been Successfully logged in', 'success')
                return redirect(url_for('views.index'))
            else: 
                flash('You have Entered the wrong password', 'danger')
                return render_template('login.html', title='Login', login=login)
        else:
            flash('The Email you entered does not exist', 'danger')
            return render_template('login.html', title='Login', login=login)


    return render_template('login.html', title = 'Login', login = login)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup = Signup()

    if signup.validate_on_submit():
        flash(f'Account for { signup.email.data } created successfully!', 'success')
        return redirect(url_for('views.index'))

    return render_template('signup.html', title = 'Sign Up', signup = signup)