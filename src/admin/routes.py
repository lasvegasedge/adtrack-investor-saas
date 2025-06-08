from flask import render_template
from flask_login import login_required, current_user
from . import admin

@admin.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        return render_template('403.html')
    return render_template('admin/index.html')