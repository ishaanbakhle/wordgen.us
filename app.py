from flask import Flask, render_template
import pandas as pd
from wordgen import generator

#Creates new instance of Flask
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("home.html", text = "")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/", methods = ["GET", "POST"])
def generate():
    df = pd.read_csv("static/out.csv").astype('float').as_matrix()
    return render_template("home.html", text = generator.generate(df))


if __name__ == '__main__':
    app.run(debug=True) #Invariant, debug=False in prod env
