from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Product
 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@supercheckerdb.cx4u2uqs8cs8.ap-southeast-2.rds.amazonaws.com:5432/Super_Checker_DB'
 
 
#Intitialize the database
db.init_app(app)
migrate=Migrate(app, db)
 
# Create a database connection
# engine = create_engine('postgresql://postgres:password@localhost:5432/superchecker-db')
# Session = sessionmaker(bind=engine)
# session = Session()
 
# Base = declarative_base()
 
 
 
@app.route("/sign_in")
def home():
    return render_template("sign_in.html")
 
@app.route("/about")
def about():
    return render_template("about.html")
 
@app.route("/shopping_list")
def shopping_list():
    return render_template("shoppinglist.html")
 
@app.route("/register")
def register():
    return render_template("register.html")
 
#This route is for testing html templates
@app.route("/test")
def test():
    return render_template("footer.html")
 
@app.route("/")
def index():
    with app.app_context():
        # item = Product.query.filter_by(name="avocado")
        # query = session.query(Product).filter(Product.name == "avocado")
           
            item = Product.query.filter_by(name="woolworths raw prawns tail on  200g")
            print(item[0].name, item[0].img)
    return render_template("index.html", main=item[0])
 
 
@app.route("/<search>")
def index_with_search(search):
    try:
        with app.app_context():
            # item = Product.query.filter_by(name="avocado")
            # query = session.query(Product).filter(Product.name == "avocado")
            like_search = "%{}%".format(search)
            item = Product.query.filter(Product.name.like(like_search)).all()
            supermarketOne = item[0]
            print(supermarketOne.name, supermarketOne.img)
            print("runnninh2")
            return render_template("index.html", main=supermarketOne)
    except:
        return redirect("/")
   
# @app.route("/product_info", methods=['POST'])
# def product_info():
#     # return "hello my g"
#     print("/productinfo func working")
#     return
       
@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method=='POST':
        term = request.form.get("searchterm")
        return redirect(f"/{term}")
 
 
 
#APIS FOR TESTING
@app.route("/signInAttempt",methods=['POST'])
def signInAttempt():
    # email=request.form['email']
    # password=request.form['password']
    # return {"email" : email, "password" : password}
 
   
    return {"status": "working I think"}
 
 
 
 
 
@app.route("/registerAttempt",methods=["POST"])
def registerAttempt():
    return{"result":"Register complete"}
 
@app.route("/anotherSuperMarket",methods=["POST"])
def anothersuperMarket():
    return{"result":"Here is new super amrket"}
 
@app.route("/addCart",methods=["POST"])
def addCart():
    return{"result":"Product in Cart"}
 
@app.route("/emptyList",methods=["POST"])
def emptyList():
    return{"result":"This list is empty"}
   
   
 
 
if __name__ == "__main__":
    app.run(debug=True)
