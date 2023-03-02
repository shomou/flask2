from flask import Flask
from app.settings.config import Ajustes, ConexionMail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import SMTPHandler
import logging

app = Flask(__name__)

app.config.from_object(Ajustes)
bdd = SQLAlchemy(app)
migrar = Migrate(app,bdd)
login = LoginManager(app)
login.login_view = 'login' # ESTO ES LO QUE NECESIMATOS
"""Por último vamos a personalizar el mensaje que genera flask por defecto para cuando un usuario intenta acceder a una página en la que necesita estar logueado y lo hacemos de la siguiente manera"""
login.login_message = 'Por favor inicia sesión para acceder a esta página.'

from app import rutas, modelos, errores

if app.debug == False:
    print('Hola1')
    if ConexionMail.MAIL_SERVER:
        autenticacion = None
    if ConexionMail.MAIL_USERNAME or ConexionMail.MAIL_PASSWORD:
        autenticacion = (ConexionMail.MAIL_USERNAME, ConexionMail.MAIL_PASSWORD)
        seguridad = None
    if ConexionMail.MAIL_USE_TLS:
        seguridad = ()
        enviar_email = SMTPHandler(
            mailhost = (ConexionMail.MAIL_SERVER, ConexionMail.MAIL_PORT),
            fromaddr = 'no-reply@' + ConexionMail.MAIL_SERVER,
            toaddrs = ConexionMail.ADMINS, subject='Fallo encontrado en nuestro Blog',
            credentials= autenticacion, secure=seguridad
        )
        enviar_email.setLevel(logging.ERROR)
        app.logger.addHandler(enviar_email)