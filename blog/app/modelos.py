from app import bdd
from datetime import datetime

class Usuario(bdd.Model):
    id = bdd.Column(bdd.Integer, primary_key=True)
    username = bdd.Column(bdd.String(64), index=True, unique=True)
    email =  bdd.Column(bdd.String(120), index=True, unique=True)
    hash_clave = bdd.Column(bdd.String(128))

    def __repr__(self):
        return '<Usuario {}>'.format(self.username)

class Pubs(bdd.Model):
    id = bdd.Column(bdd.Integer, primary_key=True)
    cuerpo = bdd.Column(bdd.String(256))
    timestamp = bdd.Column(bdd.DateTime, index=True, default=datetime.now)
    id_usuario = bdd.Column(bdd.Integer, bdd.ForeignKey('usuario.id'))

    def __repr__(self):
        return '<Publicación {}>'.format(self.cuerpo)

