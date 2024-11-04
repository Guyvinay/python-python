from flask import Flask, flash, jsonify, request, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user
from pymongo import MongoClient 
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6'
client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6')
mongo = PyMongo(app)
bcrypt = Bcrypt(app)



# app.py
db = client['mydb']

class User:
    def __init__(self, name, email, password) :
        self.name = name
        self.email = email
        self.password = password
        self.is_active = True


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve user input from the registration form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Securely hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Insert user data into the MongoDB collection (e.g., 'users')
        user = {
            'username': username,
            'email': email,
            'password': hashed_password
        }
        db.users.insert_one(user)

        # Flash a success message
        flash('Your account has been created!', 'success')

        # Redirect to the login page
        # return redirect(url_for('login'))
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve user input from the login form
        username = request.form['username']
        password = request.form['password']

        # Query the database to find the user by username
        user = db.users.find_one({'username': username})

        if user and bcrypt.check_password_hash(user['password'], password):
            # Successful login
            # user_obj = User(username, user['email'], user['password'])
            # login_user(user_obj)  # Log in the user
            return redirect(url_for('profile'))  # Redirect to user profile page

        # If login fails, show an error message
        flash('Login failed. Check your username and password.', 'error')

    # Always render the 'login.html' template, whether login is successful or not
    return render_template('login.html')


# app.py

@app.route('/profile')
@login_required  # This decorator ensures that only authenticated users can access this route
def profile():
    # Fetch user profile data
    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        # You can add more profile data as needed
    }
    return render_template('profile.html', user_data=user_data)

# users_collection = db['users']

if __name__ == '__main__':
    app.secret_key = 'your-secret-key'
    app.run(debug=True)