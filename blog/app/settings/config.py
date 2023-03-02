from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class Ajustes(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'contraseña'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config:
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Ajustes):
    DEBUG = True

class ConexionMail(object):
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'edmundo.jayr.perez.rosales@gmail.com'
    MAIL_PASSWORD = 'edMj4p390!2e'
    ADMINS = 'edmundo.jayr.perez.rosales@gmail.com'

config = {
    'development' : DevelopmentConfig
}