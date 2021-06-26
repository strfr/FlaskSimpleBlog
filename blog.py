from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def index():
    article =dict()
    return render_template("index.html", process = 1)
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True) 
