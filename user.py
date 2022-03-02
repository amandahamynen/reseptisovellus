from flask import session, request, abort
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
import os

def login(username, password, test=False):
    try:
        sql = "SELECT id, username, password, role FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        if test:
            return True
        if user is not None:
            if check_password_hash(user[2], password):
                session["username"] = user[1]
                session["user_id"] = user[0]
                session["csrf_token"] = os.urandom(16).hex()
                session["role"] = user[3]
                return True
    except:
        return False

def register(username, password):
    try:
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username, password, role) VALUES (:username, :password, :role)"
        db.session.execute(sql, {"username":username, "password":hash_value, "role":1})
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

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

def require_role(role):
    if role > session.get("role", 0):
        abort(403)

def get_role():
    return session["role"]

def get_all():
    sql = "SELECT * FROM users"
    result = db.session.execute(sql)
    users = result.fetchall()
    return users