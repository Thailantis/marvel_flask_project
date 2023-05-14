from app import app, db
from datetime import datetine
from flask_login import USerMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class User(db.Model, UserMixin):
  id = db.Column(db.String(40), primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  token = db.Column(db.String(100), nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  characters - db.relationship('Character', backref='owner', lazy=True)
  
class Character(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(500), nullable=False)
  comics_appeared_in = db.Column(db.Integer, nullable=False)
  super_power = db.Column(db.String(200), nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  owner_id = db.Column(db.String(40), db.ForeignKey('user.id'), nullable=False)

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  
class CharacterForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  description = StringField('Description')
  comics_appeared_in = StringField('Comics Appeared In')
  super_power = StringField('Super Power')
  
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
