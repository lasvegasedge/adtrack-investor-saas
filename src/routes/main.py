from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='../templates')

@main.route('/')
def home():
    return render_template('main/index.html')

@main.route('/dashboard')
def dashboard():
    return render_template('main/dashboard.html')
