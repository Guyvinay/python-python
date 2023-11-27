from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)
# client = 
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6'
client = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6')
mongo = PyMongo(app)

@app.route('/createTask', methods=['POST'])
def create_tasks():
    new_tasks = request.get_json()
    print(new_tasks)
    task = client['mydb'].tasks.insert_one(new_tasks)
    return jsonify({"id":str(task.inserted_id),"status":"Task Successfully created"})
    

if __name__ == '__main__':
    app.run(debug=True)    