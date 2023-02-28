from app import app
from flask import render_template, redirect, url_for, flash, request
from app.formularios import FormInicio
from flask_login import current_user, login_user, logout_user, login_required
from app.modelos import Usuario
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', titulo = 'Inicio')


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = FormInicio()
    if (form.validate_on_submit()):
        usuario = Usuario.query.filter_by(username=form.nombre.data).first()
        if usuario:
            if usuario.verif_clave(form.contraseña.data):                
                login_user(usuario, remember=form.recordar.data)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                        next_page = url_for('index')
                return redirect(next_page)
            else:
                flash('Usuario o contraseña inválido')                
    return render_template('iniciar_sesion.html', titulo='Iniciar Sesión', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')