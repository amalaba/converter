from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
converter_db=SQLAlchemy(app)

from converter_app import routes, models
