import getpass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv
import re

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

uri = os.getenv("DATABASE_URL")
if uri is None:
    uri = f"postgresql:///{getpass.getuser()}"
elif uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

import routes