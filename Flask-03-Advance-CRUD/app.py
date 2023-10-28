from flask import Flask, flash, request, redirect, render_template
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

@app.route('/register', methods=['GET','POST'])
def register() :
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        encoded_password = bcrypt.generate_password_hash(password).decode('utf-8')

        user = {
            'name':name,
            'email':email,
            'password':encoded_password
        }

        db.users.insert_one(user)

        # flash('Account has succesfully been created', 'success')

        return redirect('/login')
    return render_template('register.html')

# app.py

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login logic goes here
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)