from app import app
from app.settings.config import config
import logging
from logging.handlers import SMTPHandler
from app.settings.config import ConexionMail

if __name__ == '__main__':
    app.config.from_object(config['development']) 

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

    ## app.config.from_object(Ajustes)

    ##  Blueprint Section

    ##  Error Handler Section
        
    
    app.run()