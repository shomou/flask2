from flask import Flask
from app.settings.config import Ajustes
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Ajustes)
bdd= SQLAlchemy(app)
migrar=Migrate(app,bdd)

from app import rutas, modelos
