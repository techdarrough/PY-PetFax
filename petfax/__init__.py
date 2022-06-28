from flask import Flask

def createApp():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, petfax!'
    return app

    
   

    