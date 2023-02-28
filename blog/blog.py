from app import app
from app.settings.config import config

def page_not_found(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development']) 

    ##app.config.from_object(Ajustes)

    ##  Blueprint Section

    ##  Error Handler Section
    app.register_error_handler(404,page_not_found)    
    app.run()