from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


class Signup(FlaskForm):
    email = StringField('Enter Email', validators=[InputRequired()])

    password = PasswordField('Enter a Password', validators=[
                             InputRequired(), Length(min=8)])

    confirm_password = PasswordField('Confirm Password', validators=[
                                     InputRequired(), Length(min=8), EqualTo('password')])

    submit = SubmitField('Sign Up')


class Login(FlaskForm):
    email = StringField('Enter Email', validators=[InputRequired()])

    password = PasswordField('Enter a Password', validators=[InputRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
