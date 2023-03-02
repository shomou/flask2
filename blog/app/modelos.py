from app import bdd, login
from datetime import datetime
from werkzeug.security import generate_password_hash as genph
from werkzeug.security import check_password_hash as checkph
from flask_login import UserMixin
from hashlib import md5

class Usuario(UserMixin, bdd.Model):
    id = bdd.Column(bdd.Integer, primary_key=True)
    username = bdd.Column(bdd.String(64), index=True, unique=True)
    email =  bdd.Column(bdd.String(120), index=True, unique=True)
    hash_clave = bdd.Column(bdd.String(128))
    sobre_mi = bdd.Column(bdd.String(140))
    ultima_sesion = bdd.Column(bdd.DateTime, default=datetime.utcnow)
    pubs = bdd.relationship('Pubs', backref='autor', lazy='dynamic')

    def __repr__(self):
        return '<Usuario {}>'.format(self.username)
    
    def def_clave(self,clave):
        self.hash_clave = genph(clave)
    
    def verif_clave(self, clave):
        return checkph(self.hash_clave, clave)
    
    def imagen_perfil(self, tamaño):
        codigo_hash = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(codigo_hash, tamaño)

class Pubs(bdd.Model):
    id = bdd.Column(bdd.Integer, primary_key=True)
    cuerpo = bdd.Column(bdd.String(256))
    timestamp = bdd.Column(bdd.DateTime, index=True, default=datetime.now)
    id_usuario = bdd.Column(bdd.Integer, bdd.ForeignKey('usuario.id'))

    def __repr__(self):
        return '<Publicación {}>'.format(self.cuerpo)


@login.user_loader
def cargar_usuario(id):
    return Usuario.query.get(int(id))