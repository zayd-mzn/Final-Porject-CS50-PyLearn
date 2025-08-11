from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')


    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='scrypt', salt_length=16))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            flash('Account created!', category='success')
            return redirect(url_for('views.home'))


    return render_template('sign_up.html', user=current_user)

@auth.route('/settings', methods=["GET", "POST"])
@login_required
def settings():
    if request.method == 'POST':
        new_username = request.form.get('username')
        current_password = request.form.get('password')
        
        if not check_password_hash(current_user.password, current_password):
            flash('Incorrect password. Please try again.', category='error')
            return redirect(url_for('auth.settings'))

        if not new_username:
            flash('Username cannot be empty.', category='error')
            return redirect(url_for('auth.settings'))
        
        if new_username == current_user.username:
            flash('That is already your username.', category='error')
            return redirect(url_for('auth.settings'))
        
        from .models import User
        existing_user = User.query.filter_by(username=new_username).first()
        if existing_user:
            flash('This username already exists.', category='error')
            return redirect(url_for('auth.settings'))

        current_user.username = new_username
        db.session.commit()
        flash('Username updated!', category='success')
        return redirect(url_for('views.home'))

    return render_template('settings.html', user=current_user)