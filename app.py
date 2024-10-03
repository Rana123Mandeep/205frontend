from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("sign_in.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/shopping_list")
def shopping_list():
    return render_template("shoppinglist.html")



if __name__ == "__main__":
    app.run(debug=True)