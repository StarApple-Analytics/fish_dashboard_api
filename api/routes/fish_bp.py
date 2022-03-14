from flask import Blueprint
from api.controllers.FishController import store


fish_bp  = Blueprint('fish', __name__)


# CRUD routes
fish_bp.route('/fish/store', methods=['Post'])(store)