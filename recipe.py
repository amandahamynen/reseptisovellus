from sqlalchemy import true
from db import db

def add_recipe(recipe_name, recipe_type, ingredients, description):
    try:
        sql = "INSERT INTO recipes (recipe_name, recipe_type, ingredients, description) VALUES (:recipe_name, :recipe_type, :ingredients, :description)"
        db.session.execute(sql, {"recipe_name":recipe_name, "recipe_type":recipe_type, "ingredients":ingredients, "description":description})
        db.session.commit()
        return true
    except:
        return False

def get_all():
    sql = "SELECT * FROM recipes"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def search(key):
    sql = "SELECT * FROM recipes WHERE (recipe_name ILIKE :key)"
    result = db.session.execute(sql, {"key":"%" + key + "%"})
    recipes = result.fetchall()
    return recipes

def get_recipe_name(id):
    sql = "SELECT recipe_name FROM recipes WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    recipe_name = result.fetchone()[0]
    return recipe_name

def get_recipe_type(id):
    sql = "SELECT recipe_type FROM recipes WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    recipe_type = result.fetchone()[0]
    return recipe_type

def get_ingredients(id):
    sql = "SELECT ingredients FROM recipes WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    ingredients = result.fetchone()[0]
    return ingredients

def get_description(id):
    sql = "SELECT description FROM recipes WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    description = result.fetchone()[0]
    return description