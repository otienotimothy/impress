from flask import Blueprint, render_template, flash, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
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

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash(f'You have been Successfully logged in', 'success')
                return redirect(url_for('views.index'))
            else:
                flash('You have Entered the wrong password', 'danger')
                return render_template('login.html', title='Login', login=login)
        else:
            flash('The Email you entered does not exist', 'danger')
            return render_template('login.html', title='Login', login=login)

    return render_template('login.html', title='Login', login=login)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup = Signup()

    if signup.validate_on_submit():

        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user_exist = User.query.filter_by(email=email).first()

        if user_exist:

            flash(
                f'User with email {signup.email.data} already exists, login instead', 'error')
            return render_template('signup.html', title='Sign Up', signup=signup)

        else:

            if password == confirm_password:
                password_hash = generate_password_hash(password)
                user = User(email=email, password=password_hash)
                db.session.add(user)
                db.session.commit()

                flash(
                    f'Account for { signup.email.data } created successfully!', 'success')
                return redirect(url_for('views.index'))
            else:
                flash(f'Password did not match')
                return render_template('signup.html', title='Sign Up', signup=signup)

    return render_template('signup.html', title='Sign Up', signup=signup)
