from flask_sqlalchemy import SQLAlchemy
 
 
 
db = SQLAlchemy()
 
 
class Product(db.Model):
 
    __tablename__="django_superchecker_project_product"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dollars = db.Column(db.Integer)
    cents = db.Column(db.Integer)
    img= db.Column(db.String)
    link= db.Column(db.String)
 