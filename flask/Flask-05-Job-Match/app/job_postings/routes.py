from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from config import MONGO_URI
from pymongo import MongoClient
from bson import ObjectId, json_util

job_postings_bp = Blueprint('job_postings', __name__)

# Assuming you want to keep the MongoClient instance within this file
mongo = MongoClient(MONGO_URI)

job_seekers = mongo.job_machingdb.job_seekers
job_postings = mongo.job_machingdb.job_postings
hiring_managers = mongo.job_machingdb.hiring_managers
applications = mongo.job_machingdb.applications
# API routes for Job Posting CRUD operations
@job_postings_bp.route('/', methods=['GET'])
def get_job_postings():
    job_postings_list = list(job_postings.find())
    for posting in job_postings_list :
        posting['_id'] = str(posting['_id'])

    return jsonify({
        'job_postings': job_postings_list,
        'total_job_postings':len(job_postings_list)
        })

@job_postings_bp.route('/<id>', methods=['GET'])
def get_job_posting(id):
    try:
        job_posting = job_postings.find_one({'_id': ObjectId(id)})
        if job_posting:

            job_posting['_id']=str(job_posting['_id'])

            return jsonify({'job_posting': job_posting})
        else:
            return jsonify({'message': 'Job Posting not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@job_postings_bp.route('/<hiring_manager_id>', methods=['POST'])
def add_job_posting(hiring_manager_id):
    try:
        data = request.json

        hiring_manager = hiring_managers.find_one({'_id':ObjectId(hiring_manager_id)})

        if not hiring_manager :
            return jsonify({
                'error':f'Hiring Manager with id: {hiring_manager_id} not found'
            })
        
        

        data['hiring_manage_id'] = hiring_manager_id
        job_posting_id = job_postings.insert_one(data).inserted_id

        hiring_manager['job_postings'].append(str(job_posting_id))

        hiring_managers.update_one(
            {
            '_id' : ObjectId(hiring_manager['_id']),
            },
            {
               '$set':hiring_manager
            })

        return jsonify({'job_posting_id': str(job_posting_id)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@job_postings_bp.route('/<id>', methods=['PUT'])
def update_job_posting(id):
    try:
        data = request.json
        result = job_postings.update_one({'_id': ObjectId(id)}, {'$set': data})
        if result.modified_count > 0:
            return jsonify({'message': 'Job Posting updated successfully'})
        else:
            return jsonify({'message': 'Job Posting not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@job_postings_bp.route('/<id>', methods=['DELETE'])
def delete_job_posting(id):
    try:
        job_posting = job_postings.find_one({'_id':ObjectId(id)})
        print(job_posting)
        hiring_manager_id = job_posting['hiring_manage_id']

        print(hiring_manager_id)

        hiring_manager = hiring_managers.find_one(
            {'_id':ObjectId(hiring_manager_id)}
        )

        print(hiring_manager['job_postings'])

        if id in hiring_manager['job_postings'] :
            hiring_manager['job_postings'].remove(id)
            hiring_managers.update_one(
                {'_id': ObjectId(hiring_manager_id)
                 },
                 {'$set':hiring_manager}
            )
            
            

        result = job_postings.delete_one({'_id': ObjectId(id)})


        if 1 > 0:
            return jsonify({'message': 'Job Posting deleted successfully'})
        else:
            return jsonify({'message': 'Job Posting not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
#Job Posting endpoints done
