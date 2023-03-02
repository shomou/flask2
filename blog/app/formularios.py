from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

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

