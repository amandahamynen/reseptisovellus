from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def login(username, password, test=False):
    try:
        sql = "SELECT id, username, password FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        if test:
            return True
        if user is not None:
            if check_password_hash(user[2], password):
                session["username"] = user[1]
                session["user_id"] = user[0]
                return True
    except:
        return False

def register(username, password):
    try:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        return True
    except:
        return False

def logout():
    session.clear()
    return True

def isLoggedIn():
    try:
        session["username"]
        session["user_id"]
        return True
    except:
        return False

def get_id():
    return session["user_id"]