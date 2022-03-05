#template inheritance in flask
from flask import Flask,render_template

# Setting up the application

app=Flask(__name__,template_folder="template")

# making route
@app.route("/")
def home():
    return "<h1>welcome to the homepage</h1>"

@app.route("/inheritance")
def index():
    return render_template("main.html")

@app.route("/friends/<name>")
def friend(name):
    return render_template("friend.html",name=name)

#running application
if __name__=="__main__":
    app.run(debug=True)