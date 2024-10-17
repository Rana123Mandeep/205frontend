from flask import Flask, render_template


app = Flask(__name__)

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
    return render_template("index.html")

@app.route("/search")
def search():
    return render_template("search.html")

#APIS FOR TESTING
@app.route("/signInAttempt",methods=['POST'])
def signInAttempt():
    return {"result" : "It's working"}

@app.route("/registerAttempt",methods=["POST"])
def registerAttempt():
    return{"result":"Register complete"}

@app.route("/anotherSuperMarket",methods=["POST"])
def anothersuperMarket():
    return{"result":"Here is new super amrket"}

@app.route("/addCart",methods=["POST"])
def addCart():
    return{"result":"Product in Cart"}
    
    


if __name__ == "__main__":
    app.run(debug=True)