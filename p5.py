#url building in flask
#url_for()  function is used to build url dynamically for a specific function
#first argument is the name of the  function and second argument are one or more keywords corresponding to the variable part of the url
#it allows us to change the url in one go without having to remenebr to change url all over the place
# this flssk application simulates the library management system which can be used by the three types of users, i.e., admin, librarion, and student. There is a specific function named user() which recognizes the user the redirect the user to the exact function which contains the implementation for this particular function.

from flask import Flask
app=Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "<h1>this is admin page </h1>"

@app.route("/librarian")
def hello_librarian():
    return "<h1>this is librarian page </h1>"

@app.route("/student")
def hello_student():
    return "<h1>this is student page </h1>"

@app.route("/user/<name>")
def user(name):
    if user=="admin":
        return redirect(url_for("hello_admin")) 

    if user=="librarian":
        return redirect(url_for("hello_librarian")) 

    if user=="student":
        return redirect(url_for("hello_student")) 


if __name__=="__main__":
    app.run(debug=True)


