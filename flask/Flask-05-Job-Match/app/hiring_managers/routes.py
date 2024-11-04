from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from config import MONGO_URI
from pymongo import MongoClient
from bson import ObjectId, json_util

hiring_managers_bp = Blueprint('hiring_managers', __name__)

# Assuming you want to keep the MongoClient instance within this file
mongo = MongoClient(MONGO_URI)

job_seekers = mongo.job_machingdb.job_seekers
job_postings = mongo.job_machingdb.job_postings
hiring_managers = mongo.job_machingdb.hiring_managers
applications = mongo.job_machingdb.applications
@hiring_managers_bp.route('/', methods=['GET'])
def get_hiring_managers():

    try:
        hiring_managers_list = list(hiring_managers.find())
        
        for manager in hiring_managers_list :
            manager['_id'] = str(manager['_id'])

        return jsonify({
            'hiring_managers': hiring_managers_list,
            'total_hiring_managers':len(hiring_managers_list)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API routes for Hiring Manager CRUD operations
@hiring_managers_bp.route('/<id>', methods=['GET'])
def get_hiring_manager(id):
    try:
        hiring_manager = hiring_managers.find_one({'_id': ObjectId(id)})
        if hiring_manager:
            hiring_manager['_id'] = str(hiring_manager['_id'])
            return jsonify({'hiring_manager': hiring_manager})
        else:
            return jsonify({'message': 'Hiring Manager not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API routes for Hiring Manager CRUD operations
@hiring_managers_bp.route('/', methods=['POST'])
def add_hiring_manager():
    try:
        data = request.json
        data['job_postings'] = list()

        # Insert data into MongoDB
        result = hiring_managers.insert_one(data)

        # Fetch the inserted document from MongoDB using the inserted_id
        inserted_document = hiring_managers.find_one({'_id': result.inserted_id})

        inserted_document['_id'] = str(inserted_document['_id'])

        
        return jsonify({'hiring_manager':inserted_document})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
# API routes for Hiring Manager CRUD operations
@hiring_managers_bp.route('/<id>', methods=['PUT'])
def update_hiring_manager(id):
    try:
        data = request.json
        result = hiring_managers.update_one({'_id': ObjectId(id)}, {'$set': data})
        if result.modified_count > 0:
            return jsonify({'message': 'Hiring Manager updated successfully'})
        else:
            return jsonify({'message': 'Hiring Manager not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API routes for Hiring Manager CRUD operations
@hiring_managers_bp.route('/<id>', methods=['DELETE'])
def delete_hiring_manager(id):
    try:
        # hiring_managers.delete_many({'name':'Hiring Manager 12'})

        hiring_manager = hiring_managers.find_one({'_id':ObjectId(id)})
        

        for manager in hiring_manager['job_postings'] :
          print(manager)
          job_postings.delete_one(
              {'_id':ObjectId(manager)}
          )


        result = hiring_managers.delete_one(
              {'_id':ObjectId(id)}
          )

        if result.deleted_count > 0:
            return jsonify({'message': 'Hiring Manager deleted successfully'})
        else:
            return jsonify({'message': 'Hiring Manager not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
