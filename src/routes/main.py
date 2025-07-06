from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/dashboard')
def dashboard():
    return render_template('main/dashboard.html')

@main.route('/')
def home():
    stats = {
        "waitlist": 3500,
        "roi_uplift": "28%",
        "tracked_spend": "$2.3M",
        "markets": 43,
        "campaigns": 211
    }
    return render_template("main/index.html", stats=stats)
