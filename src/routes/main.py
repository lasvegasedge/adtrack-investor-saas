from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('main/index.html')

@main.route('/dashboard')
def dashboard():
    return render_template('main/dashboard.html')
    
    