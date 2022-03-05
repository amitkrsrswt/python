#dynamic routing in flask

from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return  "<h1>this is homepage </h1>"

@app.route("/about")
def about():
    return  "<h1>this is about page </h1>"

@app.route("/contact/<name>")    
def contact(name):
    return "<h2>my name is :</h2>"+name

if __name__=="__main__":
    app.run(debug=True)

