from api.services.PredictionService import PredictionService
from flask import request
from operator import itemgetter


def show():
    width, height, diagLength, horizonLength, verticalLength = itemgetter(
        "width", "height", "horizonLength", "verticalLength", "diagLength"
    )(request.json)
    return PredictionService.predict(
        width, height, diagLength, horizonLength, verticalLength
    )
