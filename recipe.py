from sqlalchemy import true
from db import db
from flask import session

def add_recipe(recipe_name, recipe_type, ingredients, description, prep_time):
    try:
        sql = "INSERT INTO recipes (recipe_name, recipe_type, ingredients, description, prep_time, likes) VALUES (:recipe_name, :recipe_type, :ingredients, :description, :prep_time, 0)"
        db.session.execute(sql, {"recipe_name":recipe_name, "recipe_type":recipe_type, "ingredients":ingredients, "description":description, "prep_time":prep_time})
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

def get_sorted_alphabetically():
    sql = "SELECT * FROM recipes ORDER BY recipe_name"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_sorted_newest():
    sql = "SELECT * FROM recipes ORDER BY id DESC"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_sorted_oldest():
    sql = "SELECT * FROM recipes ORDER BY id"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_sorted_quickest():
    sql = "SELECT * FROM recipes ORDER BY prep_time"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_sorted_popularity():
    sql = "SELECT * FROM recipes ORDER BY likes DESC"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_maincourses():
    sql = "SELECT * FROM recipes WHERE recipe_type='maincourse'"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_desserts():
    sql = "SELECT * FROM recipes WHERE recipe_type='dessert'"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_others():
    sql = "SELECT * FROM recipes WHERE recipe_type='other'"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def like_recipe(id):
    try:
        sql = "UPDATE recipes SET likes = likes + 1 WHERE id=:id"
        db.session.execute(sql, {"id": id})
        db.session.commit()
        return True
    except:
        return False

def unlike_recipe(id):
    try:
        sql = "UPDATE recipes SET likes = likes - 1 WHERE id=:id"
        db.session.execute(sql, {"id": id})
        db.session.commit()
        return True
    except:
        return False

def add_like(recipe_id):
    try:
        user_id = session["user_id"]

        def check_if_already_in_table():
            sql = "SELECT COUNT(*) FROM likes WHERE user_id=:user_id AND recipe_id=:recipe_id AND visible=0"
            result = db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id}).fetchone()[0]
            return result

        if check_if_already_in_table():
            sql = "UPDATE likes SET visible = 1 WHERE user_id=:user_id AND recipe_id=:recipe_id"
        else:
            sql = "INSERT INTO likes (user_id, recipe_id, visible) VALUES (:user_id, :recipe_id, 1)"
        db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id})
        db.session.commit()
        return True
    except:
        return False

def remove_like(recipe_id):
    try:
        user_id = session["user_id"]
        sql = "UPDATE likes SET visible = 0 WHERE user_id=:user_id AND recipe_id=:recipe_id"
        db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id})
        db.session.commit()
        return True
    except:
        return False

def is_liked(recipe_id):
    try:
        user_id = session["user_id"]
        sql = "SELECT COUNT(*) FROM likes WHERE user_id=:user_id AND recipe_id=:recipe_id AND visible=1"
        result = db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id}).fetchone()[0]
        if result:
            return True
        else:
            return False
    except:
        return False