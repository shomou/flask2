from app import bdd, login
from datetime import datetime
from werkzeug.security import generate_password_hash as genph
from werkzeug.security import check_password_hash as checkph
from flask_login import UserMixin
from hashlib import md5

## Tabla de rompimiento
seguidores = bdd.Table('seguidores',
                       bdd.Column('seguidor_id',bdd.Integer, bdd.ForeignKey('usuario.id')),
                       bdd.Column('seguido_id',bdd.Integer, bdd.ForeignKey('usuario.id'))
                       )


class Usuario(UserMixin, bdd.Model):
    id = bdd.Column(bdd.Integer, primary_key=True)
    username = bdd.Column(bdd.String(64), index=True, unique=True)
    email =  bdd.Column(bdd.String(120), index=True, unique=True)
    hash_clave = bdd.Column(bdd.String(128))
    sobre_mi = bdd.Column(bdd.String(140))
    ultima_sesion = bdd.Column(bdd.DateTime, default=datetime.utcnow)
    ## Relacion a la tabla Pubs
    pubs = bdd.relationship('Pubs', backref='autor', lazy='dynamic')
    ## Relación a la tabla seguidores
    seguido = bdd.relationship(
                    'Usuario', secondary=seguidores,
                    primaryjoin=(seguidores.c.seguidor_id == id),
                    secondaryjoin=(seguidores.c.seguido_id == id),
                    backref=bdd.backref('seguidores', lazy='dynamic'), lazy='dynamic'
                    )

    def __repr__(self):
        return '<Usuario {}>'.format(self.username)
    
    def def_clave(self,clave):
        self.hash_clave = genph(clave)
    
    def verif_clave(self, clave):
        return checkph(self.hash_clave, clave)
    
    def imagen_perfil(self, tamaño):
        codigo_hash = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(codigo_hash, tamaño)
    
    ## Comenzar a seguir y dejar de seguir
    def seguir(self, usuario):
        if not self.siguiendo(usuario):
            self.seguido.append(usuario)
    def dejar_seguir(self, usuario):
        if self.siguiendo(usuario):
            self.seguido.remove(usuario)
    def siguiendo(self, usuario):
        return self.seguido.filter(seguidores.c.seguido_id == usuario.id).count() > 0
    
    ## Obtener publicaciones de usuarios seguidos
    def pubs_seguidores(self):
        seguido = Pubs.query.join(
        seguidores, (seguidores.c.seguido_id == Pubs.id_usuario)).filter(
        seguidores.c.seguidor_id == self.id)
        pubs_propias = Pubs.query.filter_by(id_usuario=self.id)
        return seguido.union(pubs_propias).order_by(Pubs.timestamp.desc())


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


