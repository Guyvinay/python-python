from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from controller.product_controller import product_bp

app = Flask(__name__)
# db = SQLAlchemy(app)
app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True)