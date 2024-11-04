# Job Portal API
## Introduction

This is a Job Portal API that allows users to create, read, update, and delete job seekers, hiring managers, and job postings. It is built using Python Flask and MongoDB.

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies:
```
pip install flask flask-pymongo pymongo
```
4. Create a MongoDB instance and set the MONGO_URI environment variable to the connection string of your MongoDB instance.
5. Run the following command to start the API:
```
python main.py
```

## Endpoints

### Hiring Managers

* **GET /hiring_managers:** Get all hiring managers.
* **GET /hiring_managers/<id>:** Get a specific hiring manager by ID.
* **POST /hiring_managers:** Create a new hiring manager.
* **PUT /hiring_managers/<id>:** Update an existing hiring manager.
* **DELETE /hiring_managers/<id>:** Delete an existing hiring manager.

### Job Postings

* **GET /job_postings:** Get all job postings.
* **GET /job_postings/<id>:** Get a specific job posting by ID.
* **POST /job_postings/<hiring_manager_id>:** Create a new job posting for a specific hiring manager.
* **PUT /job_postings/<id>:** Update an existing job posting.
* **DELETE /job_postings/<id>:** Delete an existing job posting.

### Job Seekers

* **GET /job_seekers:** Get all job seekers.
* **GET /job_seekers/<job_seeker_id>:** Get a specific job seeker by ID.
* **POST /job_seekers:** Create a new job seeker.
* **PUT /job_seekers/<job_seeker_id>:** Update an existing job seeker.
* **DELETE /job_seekers/<job_seeker_id>:** Delete an existing job seeker.

## Usage

To use the API, you can make requests to the endpoints using a tool like curl or Postman. For example, to get all hiring managers, you can make the following request:

```
curl -X GET http://localhost:5000/hiring_managers
```

This will return a JSON object with a list of hiring managers.

## Contributing

Please feel free to contribute to the project by opening pull requests.

## License

The project is licensed under the MIT License.