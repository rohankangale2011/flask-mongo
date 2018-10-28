import json
from bson import ObjectId
from flask import Flask
from flask_pymongo import PyMongo
from config import DB_URI

app = Flask(__name__)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app.json_encoder = JSONEncoder

app.config['MONGO_URI'] = DB_URI
mongo = PyMongo(app)