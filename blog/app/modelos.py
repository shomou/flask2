from app import bdd

class Usuario(bdd.Model):
    id = bdd.Column(bdd.Integer, primary_key=True)
    username = bdd.Column(bdd.String(64), index=True, unique=True)
    email =  bdd.Column(bdd.String(120), index=True, unique=True)
    hash_clave = bdd.Column(bdd.String(128))

    def __repr__(self):
        return '<Usuario {}>'.format(self.username)