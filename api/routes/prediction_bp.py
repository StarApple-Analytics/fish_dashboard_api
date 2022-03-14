from flask import Blueprint
from api.controllers.PredictionController import show


prediction_bp  = Blueprint('prediction', __name__)


# CRUD routes
prediction_bp.route('/predict', methods=['Post'])(show)