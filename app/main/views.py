from flask import Blueprint, render_template
from flask_login import login_required
from .forms import Create_pitch

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')


@views.route('/add_pitch')
@login_required
def add_pitch():
    pitch = Create_pitch()
    return render_template('add_pitch.html', title= 'Add Pitch', new_pitch = pitch)
