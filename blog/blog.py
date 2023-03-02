from app import app
from app.settings.config import config
import logging


if __name__ == '__main__':
    app.config.from_object(config['development']) 

   

    ## app.config.from_object(Ajustes)

    ##  Blueprint Section

    ##  Error Handler Section
        
    
    app.run()