from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class Signup(FlaskForm):
    email = StringField('Enter Email', validators=[InputRequired(), Email()])

    password = PasswordField('Enter a Password', validators=[
                             InputRequired(), Length(min=8)])

    confirm_password = PasswordField('Confirm Password', validators=[
                                     InputRequired(), Length(min=8), EqualTo('password')])

    submit = SubmitField('Sign Up')