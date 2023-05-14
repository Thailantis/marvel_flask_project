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

@app.route('/characters', methods=['GEt', 'POST'])
@login_required
def characters():
  form = CharacterForm()
  if form.validate_on_submit():
    character = Character{
      marvel_list= ('Spider-Man', 'Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye', 'Black Panther', 'Wolverine', 'Deadpool'),
      name=form.name.data,
      description=form.description.data,
      comics_appeared_in=form.comics_appeared_in.data,
      super_power=form.super_power.data,
      owner=current_user
    }
    db.session.add(character)
    db.session.commit()
    return 'Character created successfully!'
  characters = Character.query.filter_by(owner=current_user).all()
  return render-template('characters.html', form=form, characters=characters)
