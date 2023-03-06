from app import app, bdd
from flask import render_template, redirect, url_for, flash, request
from app.formularios import FormInicio, FormRegistro, EditarPerfil, Publicaciones
from flask_login import current_user, login_user, logout_user, login_required
from app.modelos import Usuario, Pubs
from werkzeug.urls import url_parse
from datetime import datetime


## Index 
@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    form = Publicaciones()
    if form.validate_on_submit():
        post = Pubs(cuerpo=form.post.data, autor=current_user)
        bdd.session.add(post)
        bdd.session.commit()
        flash('Publicación enviada correctamente.')
        return redirect(url_for('index'))
    posts = current_user.pubs_seguidores().all()
    return render_template('index.html', titulo = 'Página de inicio', form=form, posts=posts)

## Login de usuarios
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

## Logout de usuarios 
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

## Registro de usuarios
@app.route('/registro', methods=['GET','POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = FormRegistro()
    if form.validate_on_submit():
        usuario = Usuario(username=form.username.data, email= form.email.data)
        usuario.def_clave(form.contraseña.data)
        bdd.session.add(usuario)
        bdd.session.commit()
        flash('Usuario registrado correctamente, ahora puedes iniciar sessión.')
        return redirect(url_for('login'))
    return render_template('registro.html',titulo='Registro', form=form)

## Perfil de usuarios
@app.route('/usuarios/<username>')
@login_required
def perfil_usuario(username):
    usuario = Usuario.query.filter_by(username=username).first_or_404()
    posts = [
        {'autor': usuario, 'cuerpo':'Test post #1'},
        {'autor': usuario, 'cuerpo':'Test post #2'}
    ]
    return render_template('usuarios.html', usuario=usuario, posts=posts)

## Editar Perfil
@app.route('/editar_perfil', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = EditarPerfil(current_user.username)
    if form.validate_on_submit():
       current_user.username = form.username.data
       current_user.sobre_mi = form.sobre_mi.data
       bdd.session.commit()
       flash('Tus cambios han sido guardados correctamente')
       return redirect(url_for('editar_perfil'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.sobre_mi.data = current_user.sobre_mi
    return render_template('editar_perfil.html', titulo='Editar Perfil', form=form)

@app.before_request
def ultima_sesion():
    if current_user.is_authenticated:
        current_user.ultima_sesion = datetime.utcnow()
        bdd.session.commit()

@app.route('/seguir/<username>')
@login_required
def seguir(username):
    usuario = Usuario.query.filter_by(username=username).first()
    if usuario is None:
        flash('Usuario {} no encontrado.'.format(username))
        return redirect(url_for('index'))
    if usuario == current_user:
        flash('¡No puedes realizar esta acción contigo mismo!')
        return redirect(url_for('perfil_usuario', username=username))
    current_user.seguir(usuario)
    bdd.session.commit()
    flash('¡Ahora estás siguiendo a {}!'.format(username))
    return redirect(url_for('perfil_usuario', username=username))

@app.route('/dejar_seguir/<username>')
@login_required
def dejar_seguir(username):
    usuario = Usuario.query.filter_by(username=username).first()
    if usuario is None:
        flash('Usuario {} no encontrado.'.format(username))
        return redirect(url_for(index))
    if usuario == current_user:
        flash('¡No puedes realizar esta acción contigo mismo!')
        return redirect(url_for('perfil_usuario', username=username))
    current_user.dejar_seguir(usuario)
    bdd.session.commit()
    flash('Dejaste de seguir a {}.'.format(username))
    return redirect(url_for('perfil_usuario', username=username))

    


@app.route('/gracias')
def gracias():
    return render_template('gracias.html')