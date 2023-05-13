from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, current_user, logout_user
from models import User, Character
frin forms import LoginForm

@app.route('/')
def index():
  return 'Welcome to the Marvel API!'

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.password == form.password.data:
      login_user(user)
      return redirect(url_for('dashboard'))
    else:
      flash('Invalid email address or password', 'error, try again')
  return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
  characters = current_user.characters
  return render_template('dashboard.html', characters=characters)

@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('login'))
