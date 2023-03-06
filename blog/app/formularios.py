from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms import TextAreaField
from wtforms.validators import Length
from app.modelos import Usuario

class FormInicio(FlaskForm):
    nombre = StringField('Usuario', validators=[DataRequired(message='Se requiere que completes este campo')])
    contraseña = PasswordField('Contraseña',validators=[DataRequired(message='Se requiere que completes este campo')])
    recordar = BooleanField('Recordar usuario')
    enviar = SubmitField('Iniciar Sesión')

# Formularios para registro de usuarios
class FormRegistro(FlaskForm):
    username= StringField('Nombre de Usuario', validators=[DataRequired()])
    email =  StringField('Email', validators=[DataRequired(), Email()])
    contraseña =  PasswordField('Contraseña', validators=[DataRequired()])
    contraseña2 = PasswordField('Repita su Contraseña', validators=[DataRequired(),EqualTo('contraseña', 'Las contraseñas no coinciden')])
    submit = SubmitField('Registrar')


## Fromulario para editor de perfil
class EditarPerfil(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    sobre_mi = TextAreaField('Sobre mi', validators=[Length(min=0, max=140)])
    submit = SubmitField('Enviar')
    
    def __init__(self, usuarioActual, *args, **kwargs):
        super(EditarPerfil, self).__init__(*args, **kwargs)
        self.usuarioActual = usuarioActual
    def validate_username(self, username):
        if username.data != self.usuarioActual:
            usuario = Usuario.query.filter_by(username=self.username.data).first()
            if usuario is not None:
                raise ValidationError('El nombre de usuario ya existe, por favor intenta con otro.')

## Formulario publicaciones
class Publicaciones(FlaskForm):
    post = TextAreaField("Escribee algo al mundo", validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Twittear')


