from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(100), nullable=False, default='Unknown')



    def __repr__(self):
        return f"<Game: {self.name}>"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(254), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
    
    def __repr__(self):
        return f"<User: {self.username}>"