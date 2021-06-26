from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def index():
    articles = [
        {"id":1, "title":"Title1","content":"Content1"},
        {"id":2, "title":"Title2","content":"Content2"},
        {"id":3, "title":"Title3","content":"Content3"}
    ]
    return render_template("index.html", articles = articles)
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True) 
