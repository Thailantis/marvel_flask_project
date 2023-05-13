from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marvel_api import app, routes

from routes import *

app = Flask(__name__)
app.config.from_dotenv()

db - SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
