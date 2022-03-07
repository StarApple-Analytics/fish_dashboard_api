from flask import Blueprint
from api.controllers.DashboardController import index



dashboard_bp  = Blueprint('dashboard', __name__)


# CRUD routes
dashboard_bp.route('/dashboard', methods=['GET'])(index)