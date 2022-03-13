from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .forms import Create_pitch, Add_comment
from app.models import Pitch, Comment
from app import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    pitches = Pitch.query.all()
    title = 'A List of Amazing Pitches'
    create_comment = Add_comment()
    return render_template('index.html', title=title, pitches=pitches, create_comment=create_comment)

@views.route('/pitches/<category>')
def search_by_category(category):
    
    if category == 'pick_up':
        title_text = 'Pick Up Lines'
    elif category == 'product':
        title_text = 'Product Pitches'
    else:
        title_text = 'Sales Pitches'

    pitches = Pitch.query.filter_by(pitch_category=category).all()

    title = f'A list of Amazing {title_text} '
    return render_template('index.html', title=title, pitches=pitches)


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

@views.route('/my_pitches')
@login_required
def user_pitches():
    pitches = Pitch.query.filter_by(author=current_user.id)
    title = 'My Pitches'
    return render_template('user_posts.html', title =title, pitches = pitches)

@views.route('/add_comment/<pitch_id>', methods=['POST'])
@login_required
def add_comment(pitch_id):

    pitches = Pitch.query.all()
    title = 'A List of Amazing Pitches'

    create_comment = Add_comment()

    pitch = Pitch.query.filter_by(id = pitch_id).first()

    if pitch:
        comment = request.form.get('comment')

        comment_item = Comment(comment=comment, comment_author = current_user.id, comment_pitch = pitch.id)
        db.session.add(comment_item)
        db.session.commit()

        flash('Comment Added Successfully', 'success')

        print(pitch.comments)

    else:
        flash(f'The Pitch you are trying to comment on does not exist', 'danger')

    return render_template('index.html', title=title, pitches=pitches, create_comment = create_comment)



@views.route('/delete/<pitch_id>')
@login_required
def delete_pitch(pitch_id):
    pitches = Pitch.query.filter_by(author=current_user.id)
    title = 'My Pitches'
    pitch = Pitch.query.filter_by(id = pitch_id).first()

    if pitch:
        db.session.delete(pitch)
        db.session.commit()
        flash('Pitch has been successfully deleted', 'success')
    else:
        flash('Selected Pitch does not exist', 'danger')

    return render_template('user_posts.html', title=title, pitches=pitches)
