from sqlalchemy import true
from db import db
from flask import session

def add_recipe(recipe_name, recipe_type, ingredients, description, prep_time):
    try:
        user_id = session["user_id"]
        sql = """INSERT INTO recipes (recipe_name, recipe_type, ingredients, description, prep_time, likes, visible, creator) 
                 VALUES (:recipe_name, :recipe_type, :ingredients, :description, :prep_time, 0, 1, :user_id)"""
        db.session.execute(sql, {"recipe_name":recipe_name, "recipe_type":recipe_type, "ingredients":ingredients, 
                                 "description":description, "prep_time":prep_time, "user_id":user_id})
        db.session.commit()
        return true
    except:
        return False

def get_all():
    sql = "SELECT * FROM recipes WHERE visible=1"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def search(key):
    sql = """SELECT DISTINCT recipes.id, recipes.recipe_name FROM recipes, users 
             WHERE (users.username ILIKE :name_key AND users.id=recipes.creator 
             AND recipes.visible=1) OR (recipe_name ILIKE :key AND recipes.visible=1)"""
    result = db.session.execute(sql, {"name_key":key+"%", "key":"%" + key + "%"})
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

def get_prep_time(id):
    sql = "SELECT prep_time FROM recipes WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    description = result.fetchone()[0]
    return description

def get_creator(id):
    sql = """SELECT users.username FROM recipes, users 
             WHERE recipes.creator=users.id AND recipes.id=:id"""
    result = db.session.execute(sql, {"id": id})
    creator = result.fetchone()[0]
    return creator

def get_sorted_alphabetically():
    sql = "SELECT * FROM recipes WHERE visible=1 ORDER BY recipe_name"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_sorted_newest():
    sql = "SELECT * FROM recipes WHERE visible=1 ORDER BY id DESC"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_sorted_oldest():
    sql = "SELECT * FROM recipes WHERE visible=1 ORDER BY id"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_sorted_quickest():
    sql = "SELECT * FROM recipes WHERE visible=1 ORDER BY prep_time"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_sorted_popularity():
    sql = "SELECT * FROM recipes WHERE visible=1 ORDER BY likes DESC"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_maincourses():
    sql = "SELECT * FROM recipes WHERE recipe_type='maincourse' AND visible=1"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_desserts():
    sql = "SELECT * FROM recipes WHERE recipe_type='dessert' AND visible=1"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_others():
    sql = "SELECT * FROM recipes WHERE recipe_type='other' AND visible=1"
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
            sql = """SELECT COUNT(*) FROM likes WHERE user_id=:user_id 
                     AND recipe_id=:recipe_id AND visible=0"""
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
        sql = """SELECT COUNT(*) FROM likes 
                 WHERE user_id=:user_id AND recipe_id=:recipe_id AND visible=1"""
        result = db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id}).fetchone()[0]
        if result:
            return True
        else:
            return False
    except:
        return False

def add_favourite(recipe_id):
    try:
        user_id = session["user_id"]

        def check_if_already_in_table():
            sql = """SELECT COUNT(*) FROM favourites 
                     WHERE user_id=:user_id AND recipe_id=:recipe_id AND visible=0"""
            result = db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id}).fetchone()[0]
            return result

        if check_if_already_in_table():
            sql = "UPDATE favourites SET visible = 1 WHERE user_id=:user_id AND recipe_id=:recipe_id"
        else:
            sql = """INSERT INTO favourites (user_id, recipe_id, visible) 
                  VALUES (:user_id, :recipe_id, 1)"""
        db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id})
        db.session.commit()
        return True
    except:
        return False

def remove_favourite(recipe_id):
    try:
        user_id = session["user_id"]
        sql = "UPDATE favourites SET visible = 0 WHERE user_id=:user_id AND recipe_id=:recipe_id"
        db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id})
        db.session.commit()
        return True
    except:
        return False

def is_favourite(recipe_id):
    try:
        user_id = session["user_id"]
        sql = """SELECT COUNT(*) FROM favourites 
                 WHERE user_id=:user_id AND recipe_id=:recipe_id AND visible=1"""
        result = db.session.execute(sql, {"user_id": user_id, "recipe_id": recipe_id}).fetchone()[0]
        if result:
            return True
        else:
            return False
    except:
        return False

def hide_recipe(recipe_id):
    try:
        role = session["role"]

        def check_if_already_in_table():
            sql = "SELECT COUNT(*) FROM recipes WHERE id=:recipe_id AND visible=1"
            result = db.session.execute(sql, {"recipe_id": recipe_id}).fetchone()[0]
            return result

        if role == 2:
            if check_if_already_in_table():
                sql = "UPDATE recipes SET visible=0 WHERE id=:recipe_id"
                db.session.execute(sql, {"recipe_id": recipe_id})
                db.session.commit()
                return True
            else:
                return False
        else:
            return False
    except:
        return False

def return_recipe(recipe_id):
    try:
        role = session["role"]

        def check_if_already_in_table():
            sql = "SELECT COUNT(*) FROM recipes WHERE id=:recipe_id AND visible=0"
            result = db.session.execute(sql, {"recipe_id": recipe_id}).fetchone()[0]
            return result

        if role == 2:
            if check_if_already_in_table():
                sql = "UPDATE recipes SET visible=1 WHERE id=:recipe_id"
                db.session.execute(sql, {"recipe_id": recipe_id})
                db.session.commit()
                return True
            else:
                return False
        else:
            return False
    except:
        return False

def get_hidden():
    sql = "SELECT * FROM recipes WHERE visible=0"
    result = db.session.execute(sql)
    recipes = result.fetchall()
    return recipes

def get_comments(recipe_id):
    sql = """SELECT users.username, comments.comment, comments.created_at, comments.id 
             FROM users, comments WHERE users.id=comments.creator AND comments.recipe_id=:recipe_id 
             AND comments.visible=1 ORDER BY comments.created_at"""
    comments = db.session.execute(sql, {"recipe_id": recipe_id}).fetchall()
    return comments

def add_comment(recipe_id, comment):
    try:
        user_id = session["user_id"]
        sql = """INSERT INTO comments (recipe_id, creator, comment, created_at, visible) 
              VALUES (:recipe_id, :creator, :comment, NOW(), 1)"""
        db.session.execute(sql, {"recipe_id": recipe_id, "creator": user_id, "comment": comment})
        db.session.commit()
        return True
    except:
        return False

def rate(recipe_id, rating):
    try:
        user_id = session["user_id"]
        def check_if_user_already_rated():
            sql = "SELECT COUNT(*) FROM ratings WHERE user_id=:user_id and recipe_id=:recipe_id"
            result = db.session.execute(sql, {"user_id": user_id, "recipe_id":recipe_id}).fetchone()[0]
            return result
        is_rated = check_if_user_already_rated()
        if is_rated == 0:
            sql = "INSERT INTO ratings (recipe_id, user_id, rating) VALUES (:recipe_id, :user_id, :rating)"
            db.session.execute(sql, {"recipe_id":recipe_id, "user_id":user_id, "rating":rating})
            db.session.commit()
            return True
        else:
            sql = "UPDATE ratings SET rating=:rating WHERE user_id=:user_id AND recipe_id=:recipe_id"
            result = db.session.execute(sql, {"rating":rating, "user_id": user_id, "recipe_id":recipe_id})
            db.session.commit()
            return True
    except:
        return False

def calculate_rating(recipe_id):
    try:
        sql = "SELECT ROUND(AVG(rating), 1) FROM ratings WHERE recipe_id=:recipe_id"
        average = db.session.execute(sql, {"recipe_id": recipe_id}).fetchone()[0]
        return average
    except:
        return 0

def count_ratings(recipe_id):
    sql = "SELECT COUNT(*) FROM ratings WHERE recipe_id=:recipe_id"
    count = db.session.execute(sql, {"recipe_id":recipe_id}).fetchone()[0]
    return count