from flask import render_template 
from app import app, bdd

@app.errorhandler(404)
def pagina_noencontrada(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def error_interno(error):
    bdd.session.rollback()
    return render_template('500.html'),500