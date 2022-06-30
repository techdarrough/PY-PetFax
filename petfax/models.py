from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()
#can create more model in own file and import here
class Fact(db.Model):
    __tablename__ =  'facts' 
    
    id = db.Column(db.Integer, primary_key = True) 
    submitter = db.Column(db.String(250)) 
    fact = db.Column(db.Text) 

    