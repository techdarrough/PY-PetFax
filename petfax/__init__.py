from flask import Flask
from flask_migrate import Migrate


#aap factory
def createApp():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return 'Hello, petfax!'

    #register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import facts
    app.register_blueprint(facts.bp)

    

    #return the app
        

    
    return app

    
   

    