from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

from routes.main import main

app = Flask(__name__)

app.register_blueprint(main)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret')

if __name__ == '__main__':
    app.run(debug=True)
