from app import app
from flask import render_template, redirect, url_for, flash
from app.formularios import FormInicio

@app.route('/')
@app.route('/index')
def index():
    usuario = {'nombre':'Jayr'}
    titulo = 'Inicio'
    pubs = [
        {
            'autor':{'usuario':'Jayr'},
            'pub': 'Gran día en CDMX'
        },
        {
            'autor':{'usuario':'Edmundo'},
            'pub': 'Hoy me chingue unos takeshis!!'
        }
    ]
    return render_template('index.html', titulo = titulo, usuario = usuario, pubs=pubs)


@app.route('/login', methods=['GET','POST'])
def login():
    form = FormInicio()
    if (form.validate_on_submit()):
        flash('Inicio de sesión solicitado por el usuario {}, recordar={}'.format(form.nombre.data, form.recordar.data))
        return redirect(url_for('gracias'))
    return render_template('iniciar_sesion.html', titulo='Iniciar Sesión', form=form)

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')