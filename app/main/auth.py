from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import Signup, Login

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    login = Login()
    return render_template('login.html', title = 'Login', login = login)

@auth.route('/signup')
def signup():
    signup = Signup()

    if signup.validate_on_submit():
        flash(f'Account for { login.email.data } created successfully!', 'success')
        return redirect(url_for('views.index'))

    return render_template('signup.html', title = 'Sign Up', signup = signup)