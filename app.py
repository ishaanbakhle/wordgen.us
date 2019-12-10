from flask import Flask, render_template

#Creates new instance of Flask
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/", methods = ["GET", "POST"])
def generate():
    return "Generated"

if __name__ == '__main__':
    app.run(debug=True) #Invariant, debug=False in prod env
