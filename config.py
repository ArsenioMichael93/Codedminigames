import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY =  os.environ.get('SECRET_KEY')
    if os.environ.get('DATABASE_URL').startswith('postgres'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
    SQLALCHELMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHELMY_TRACK_MODIFICATIONS = False
