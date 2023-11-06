from flask import Flask, flash, jsonify, request, redirect, render_template
from flask_login import current_user
from pymongo import MongoClient 
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6'
client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6')
mongo = PyMongo(app)
bcrypt = Bcrypt(app)


class User:
    def __init__(self, name, email, password) :
        self.name = name
        self.email = email
        self.password = password

db = client['mydb']
# users_collection = db['users']

#WebService

@app.route('/register', methods=['POST'])
def register() :
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']

    encoded_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user = {
        'name':name,
        'email':email,
        'password':encoded_password
    }
    persisted_user = db.users.insert_one(user)
    # print(persisted_user.acknowledged)
    return jsonify(
        {'message':'User Registration successful', 
         'user_id':str(persisted_user.inserted_id),
         'Status':persisted_user.acknowledged,
         'user':str(user)
         })


if __name__ == '__main__':
    app.run(debug=True)