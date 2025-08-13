from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Lesson, UserProgress
from . import db

views = Blueprint("views", __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route("/lessons")
@login_required
def lessons():
    lessons = Lesson.query.all()
    user_progress = UserProgress.query.filter_by(user_id=current_user.id).all()
    progress_dict = {p.lesson_id: p.completed for p in user_progress}

    return render_template(
        "lessons.html",
        lessons=lessons,
        progress=progress_dict,
        user=current_user
    )

@views.route('/lesson')
@login_required
def lesson():
    lesson = Lesson.query.first()
    progress = UserProgress.query.filter_by(user_id=current_user.id,lesson_id=1).first()
    return render_template('lesson.html', lesson=lesson, user=current_user, progress=progress)

@views.route('/lesson2')
@login_required
def lesson2():
    progress = UserProgress.query.filter_by(user_id=current_user.id, lesson_id=2).first()
    
    return render_template('lesson2.html', user=current_user, progress=progress)

