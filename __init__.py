from flask import Flask
from flask_pymongo import PyMongo
from config import DB_URI

app = Flask(__name__)

app.config['MONGO_URI'] = DB_URI
mongo = PyMongo(app)