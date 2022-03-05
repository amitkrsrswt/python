#control flow statements in jing2 template engine

from flask import Flask,render_template

app=Flask(__name__,template_folder="template")

@app.route("/")
def home():
    return "<h1>welcome to the home page   </h1>"

@app.route("/display")   
def show():
     list1=["aman","amit","tinku","modi","yogi"]
     dict={"maths":65,"english":98,"digital":88,"sanskrit":78}
     return render_template("control.html",list1=list1,dict=dict)

if __name__=="__main__":
    app.run(debug=True)     