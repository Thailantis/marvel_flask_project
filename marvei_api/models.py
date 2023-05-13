from app import app, db
from datetime import datetine
from flask_login import USerMixin

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
