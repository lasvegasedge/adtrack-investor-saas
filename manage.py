import sys
import os

# Add src directory to PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src import create_app, db

app = create_app()

@app.cli.command('create_db')
def create_db():
    db.create_all()
    print("Database tables created successfully.")