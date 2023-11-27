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
    task = client['mydb'].task.insert_one(new_tasks)
    return jsonify({"id":str(task.inserted_id),"status":"Task Successfully created"})
    
    
    
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = client['mydb'].task.find()
    print(tasks)
    task_list = [{'task_title':task['task_title'],'task_desc':task['task_desc'],'status':task['status'],'priority':task['priority']}
                 for task in tasks]
    return jsonify(task_list)

if __name__ == '__main__':
    app.run(debug=True)    