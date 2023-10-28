
Create a New Directory: Start by creating a new directory for your project and navigate to it in your command line.

Set Up a Virtual Environment: Create a virtual environment for your project to isolate dependencies.
-> python -m venv venv
-> venv\Scripts\activate 
-> source venv/bin/activate  # On Mac

Install Flask and Required Packages: Install Flask and additional packages you'll need for this project. You'll want Flask-SQLAlchemy for database management and a password hashing library (e.g., Flask-Bcrypt) for secure password storage.

-> pip install Flask Flask-SQLAlchemy Flask-Bcrypt