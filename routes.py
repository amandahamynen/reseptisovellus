from crypt import methods
from flask import render_template, request, redirect
from app import app
from app import db
import user

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if user.isLoggedIn():
        return redirect("/")
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        re_password = request.form["re_password"]
        if username == "" or password == "":
            return render_template("/register.html", message="Kenttää ei voi jättää tyhjäksi")
        if password != re_password:
            return render_template("/register.html", message="Salasanat eivät vastanneet toisiaan")
        if user.register(username, password):
            if user.login(username, password):
                return redirect("/")
        else:
            return render_template("/register.html", message="Rekisteröinti ei onnistunut")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    if user.isLoggedIn():
        return redirect("/")
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.login(username, password):
            print("kirjauduttu")
            return redirect("/")
        else:
            return render_template("/login.html", message="Kirjautuminen ei onnistunut")

@app.route("/logout")
def logout():
    user.logout()
    return redirect("/")