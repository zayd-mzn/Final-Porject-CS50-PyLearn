from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Lesson

views = Blueprint("views", __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/lesson')
@login_required
def lesson():
    lesson = Lesson.query.first()
    return render_template('lesson.html', lesson=lesson, user=current_user)