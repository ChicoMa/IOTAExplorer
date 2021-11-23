from IOTAExplorer import IOTAExplorer
from flask import render_template

IOTAExplorer.route("/admin/dashboard")
def admin_dashboard():
    return render_template("/admin/dashboard.html")