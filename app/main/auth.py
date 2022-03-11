from crypt import methods
from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import Signup, Login

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login = Login()

    if login.validate_on_submit():
        flash(f'You have been Successfully logged in', 'success')
        return redirect(url_for('views.index'))

    return render_template('login.html', title = 'Login', login = login)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup = Signup()

    if signup.validate_on_submit():
        flash(f'Account for { signup.email.data } created successfully!', 'success')
        return redirect(url_for('views.index'))

    return render_template('signup.html', title = 'Sign Up', signup = signup)