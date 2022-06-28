from atexit import register
from flask import Flask

def createApp():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, petfax!'

    #register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    #return the app
        

    
    return app

    
   

    