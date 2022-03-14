from flask import Blueprint
from api.controllers.PredictionController import view


prediction_bp  = Blueprint('prediction', __name__)


# CRUD routes
prediction_bp.route('/predict', methods=['Post'])(view)