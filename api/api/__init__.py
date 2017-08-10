#Imports
from flask import Flask
from flask_pymongo import PyMongo
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config.from_object("config")
mongo = PyMongo(app)
auth = HTTPBasicAuth()

from api import views