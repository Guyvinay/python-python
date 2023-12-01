from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from config import MONGO_URI
from pymongo import MongoClient
from bson import ObjectId




app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo = MongoClient(app.config['MONGO_URI'])

#Creating database and modals
job_seekers = mongo.job_machingdb.job_seekers

#routes to initialze collections and add some data
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

#Routes for Job_seekers CRUD Operations

#to get all job seekers
@app.route('/job_seekers', methods=['GET'])
def get_all_job_seekers():
    job_seekers_list = list(job_seekers.find())
    return jsonify({
        'job_seekers':str(job_seekers_list)
    })

@app.route('/job_seekers/<job_seeker_id>')
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


@app.route('/job_seekers', methods=['POST'])
def create_job_seeker():
    try:
        data = request.json
        job_seeker_id = job_seekers.insert_one(data).inserted_id
        return jsonify({'job_seeker_id': str(job_seeker_id)})
    except Exception as exp :
        return jsonify({
            'error':str(exp)
        }), 500

@app.route('/job_seekers/<job_seeker_id>', methods=['PUT'])
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

@app.route('/job_seekers/<job_seeker_id>', methods=['DELETE'])
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



if __name__ == '__main__':
    app.run(debug=True)