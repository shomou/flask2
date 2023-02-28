from decouple import config
import os

class Ajustes(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'contraseña'

class Config:
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Ajustes):
    DEBUG = True

config = {
    'development' : DevelopmentConfig
}