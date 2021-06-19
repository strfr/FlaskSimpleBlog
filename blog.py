from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def index():
    article =dict()
    article["title"] = "Some Title"
    article["body"] = "Body Sample"
    article["author"] = "Somebody"
    return render_template("index.html",article = article)
@app.route("/about")
def about():
    return "about"
if __name__ == "__main__":
    app.run(debug=True) 
