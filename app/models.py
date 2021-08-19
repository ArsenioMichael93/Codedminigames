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



class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(100), nullable=False, default='Unknown')
    genre = db.Column(db.String(100), nullable=True, default='Unknown')
    band = db.Column(db.String(100), nullable=True, default='Unknown')
    playlist =  db.Column(db.String(500), nullable=True, default='UnKnown')


    def __repr__(self):
        return f"<Music: {self.name}>"

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