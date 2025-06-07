from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Basic config — you can adjust this later
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a strong secret

    db.init_app(app)

    # Import Blueprints here if you have them later
    # from .auth.routes import auth
    # app.register_blueprint(auth)

    return app