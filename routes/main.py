from flask import Blueprint, jsonify
from __init__ import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    user_cursor = mongo.db.User.find()
    user_list = [doc for doc in user_cursor]
    return jsonify(data = user_list)