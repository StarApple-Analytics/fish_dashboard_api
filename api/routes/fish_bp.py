from flask import Blueprint
from api.controllers.FishController import store, show


fish_bp  = Blueprint('fish', __name__)


# CRUD routes
fish_bp.route('/fish/store', methods=['Post'])(store)
fish_bp.route('/fish/search', methods=['GET'])(show)