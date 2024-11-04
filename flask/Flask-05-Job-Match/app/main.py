from flask import Flask
from job_seekers.routes import job_seekers_bp
from job_postings.routes import job_postings_bp
from hiring_managers.routes import hiring_managers_bp
from flask_pymongo import PyMongo
from pymongo import MongoClient
from config import MONGO_URI

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
# mongo = MongoClient(app.config['MONGO_URI'])

app.register_blueprint(job_seekers_bp, url_prefix='/job_seekers')
app.register_blueprint(job_postings_bp, url_prefix='/job_postings')
app.register_blueprint(hiring_managers_bp, url_prefix='/hiring_managers')

if __name__ == '__main__':
    app.run(debug=True)
