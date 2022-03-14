from api.services.FishService import FishService
from flask import request
from operator import itemgetter


def store():

    if len(request.files) == 0:
        fishes_data = request.json.get("fishes", [])
        return FishService.upload(fishes_data)
    else:
        fishesFile= request.files["fishes_upload_sheet"]
        return FishService.uploadFile(fishesFile)


def show():
    try:
        species = itemgetter('species')(request.args)
        return FishService.search(species)
    except Exception as e:
        return {"error": e.message}
