from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from config import MONGO_URI
from pymongo import MongoClient
from bson import ObjectId, json_util

job_seekers_bp = Blueprint('job_seekers', __name__)

# Assuming you want to keep the MongoClient instance within this file
mongo = MongoClient(MONGO_URI)
job_seekers = mongo.job_machingdb.job_seekers

@job_seekers_bp.route('/', methods=['GET'])
def get_all_job_seekers():
    job_seekers_list = list(job_seekers.find())
    return jsonify({
        'job_seekers':str(job_seekers_list)
    })

@job_seekers_bp.route('/<job_seeker_id>')
def get_job_seeker_by_id(job_seeker_id) : 
    # print(job_seeker_id)
    # job_seeker_id_object = ObjectId(job_seeker_id)
    try :
         job_seeker = job_seekers.find_one({'_id': ObjectId(job_seeker_id)})
         if job_seeker :
            return jsonify({
               'job_seeker':str(job_seeker)
              })
         else : 
             return jsonify({
            'error':f'Job Seeker with id:{job_seeker_id} not found'
        })
    
    except Exception as exp :
        return jsonify({
            'error':str(exp)
        }), 500


@job_seekers_bp.route('/', methods=['POST'])
def create_job_seeker():
    try:
        data = request.json
        job_seeker_id = job_seekers.insert_one(data).inserted_id
        return jsonify({'job_seeker_id': str(job_seeker_id)})
    except Exception as exp :
        return jsonify({
            'error':str(exp)
        }), 500

@job_seekers_bp.route('/<job_seeker_id>', methods=['PUT'])
def update_job_seeker(job_seeker_id) :
    try :
        data = request.json
        result = job_seekers.update_one(
            {'_id':ObjectId(job_seeker_id)},
            {'$set':data}
        )
        if result.modified_count > 0 :
            return jsonify(
                {'message': 'Job Seeker updated successfully'}
                )
        else : 
            return {'error': 'Job Seeker updation failed!!'}
        
    except Exception as exp :
        return jsonify({'error':str(exp)}),500    

@job_seekers_bp.route('/<job_seeker_id>', methods=['DELETE'])
def delete_job_seeker_by_id(job_seeker_id) :
    try :
        result = job_seekers.delete_one(
            {'_id':ObjectId(job_seeker_id)}
        )
        if result.deleted_count > 0 :
            return jsonify({'message': 'Job Seeker deleted successfully'})
        else:
            return jsonify({'message': 'Job Seeker not found'}), 404
    
    except Exception as exp :
        return jsonify({'error':str(exp)}), 500

# ... other routes

