from flask import Blueprint, render_template
from .forms import Signup, Login

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    login = Login()
    return render_template('login.html', title = 'Login', login = login)

@auth.route('/signup')
def signup():
    signup = Signup()
    return render_template('signup.html', title = 'Sign Up', signup = signup)