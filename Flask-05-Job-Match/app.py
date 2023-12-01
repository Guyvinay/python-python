from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from config import MONGO_URI
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.6'
mongo = MongoClient(app.config['MONGO_URI'])
# mongo = PyMongo(app)

job_seekers = mongo.mydb.job_seekers

@app.route('/modal_init', methods=['GET'])
def modal_init() :
    init_modals = [
        {"name": "John Doe", "status": "Active", "skills": "Python, Flask", "experience": "Mid Level", "bio": "Passionate developer", "availability": "2023-12-01"},
        {"name": "Jane Smith", "status": "Inactive", "skills": "Java, Spring", "experience": "Senior", "bio": "Experienced software engineer", "availability": "2023-12-01"}
    ]
    job_seekers.insert_many(init_modals)
    return jsonify({
        'status':'Database-modal-initialized',
        'data':str(init_modals)
    })



if __name__ == '__main__':
    app.run(debug=True)