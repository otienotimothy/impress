from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .forms import Create_pitch
from app.models import Pitch
from app import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')


@views.route('/add_pitch', methods= ['GET', 'POST'])
@login_required
def add_pitch():
    pitch = Create_pitch()

    if pitch.validate_on_submit():
        pitch_category = request.form.get('pitch_category')
        pitch_text = request.form.get('pitch')

        pitch_item = Pitch(pitch_category=pitch_category, pitch=pitch_text, author= current_user.id)

        db.session.add(pitch_item)
        db.session.commit()

        flash(f'Your Pitch has been added successfully.', 'success')

        pitch.pitch.data = " "

    return render_template('add_pitch.html', title= 'Add Pitch', new_pitch = pitch)
