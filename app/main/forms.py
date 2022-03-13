from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, EqualTo


class Signup(FlaskForm):
    email = StringField('What\'s your Email', validators=[InputRequired(), Email()])

    username = StringField('Add a Username', validators=[InputRequired()])

    password = PasswordField('Add a Password', validators=[
                             InputRequired(), Length(min=8)])

    confirm_password = PasswordField('Confirm Password', validators=[
                                     InputRequired(), Length(min=8), EqualTo('password')])

    submit = SubmitField('Sign Up')


class Login(FlaskForm):
    email = StringField('Enter Email', validators=[InputRequired(), Email()])

    password = PasswordField('Enter a Password', validators=[
                             InputRequired(), Length(min=8)])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


class Create_pitch(FlaskForm):
    pitch_category = SelectField('Category', choices=[(
        'pick_up', 'Pick up Lines'), ('product', 'Product Pitch'), ('sales', 'Sales Pitch')], validators=[InputRequired()])

    pitch = TextAreaField('What\'s your Pitch', validators=[InputRequired()])

    submit = SubmitField('Create')

class Add_comment(FlaskForm):
    comment = StringField('Comment', validators=[InputRequired(), Length(max=200)])

    submit = SubmitField('Comment')