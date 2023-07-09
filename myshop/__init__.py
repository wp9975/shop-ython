from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from myshop import views, models

with app.app_context():
    db.create_all()

from flask_login import LoginManager
from .models import User

login = LoginManager(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
