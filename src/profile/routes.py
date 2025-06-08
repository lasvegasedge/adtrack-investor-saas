from flask import render_template
from flask_login import login_required
from . import profile

@profile.route('/account')
@login_required
def account():
    return render_template('profile/profile.html')