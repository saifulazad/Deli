__author__ = 'SADI'

from flask.ext.sqlalchemy import SQLAlchemy

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)


from app import views, models