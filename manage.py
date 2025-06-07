from src import create_app, db

app = create_app()

@app.cli.command('create_db')
def create_db():
    db.create_all()
    print("Database tables created successfully.")
