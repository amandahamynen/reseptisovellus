from flask import render_template, request, redirect
from app import app
from app import db
import user
import recipe

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        key = request.form.get("key")
        if key == "" or key.strip() == "":
            return render_template("index.html")
        return redirect(f"/search/{key}")
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
            return redirect("/")
        else:
            return render_template("/login.html", message="Kirjautuminen ei onnistunut")

@app.route("/logout")
def logout():
    user.logout()
    return redirect("/")

@app.route("/new_recipe", methods=["GET", "POST"])
def new_recipe():
    if not user.isLoggedIn():
        return redirect("/")
    if request.method == "GET":
        return render_template("new_recipe.html")
    if request.method == "POST":
        recipe_name = request.form["recipe_name"]
        recipe_type = request.form.get("recipe_type")
        ingredients = request.form["ingredients"]
        ingredients = [i.strip() for i in ingredients.split("\n") if i.strip() != ""]
        description = request.form["description"]
        if recipe_name == "" or recipe_type == None or not ingredients:
            return render_template("new_recipe.html", message="Täytä vaadittavat kohdat")
        if recipe.add_recipe(recipe_name, recipe_type, ingredients, description):
            return redirect("/")
        return render_template("/new_recipe.html", message="Jokin meni pieleen, yritä uudelleen!")
    else:
        return render_template("/new_recipe.html", message="Lisääminen ei onnistunut")

@app.route("/search/<string:key>", methods=["GET", "POST"])
def search(key):
    recipes = recipe.search(key)
    return render_template("search.html", recipes=recipes, key=key)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe_id(id):
    recipe_name = recipe.get_recipe_name(id)
    ingredients = recipe.get_ingredients(id)
    description = recipe.get_description(id)
    return render_template("recipe.html", id=id, recipe_name=recipe_name, ingredients=ingredients, description=description)
    