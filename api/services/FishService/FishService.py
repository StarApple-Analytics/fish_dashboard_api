from numpy import diag
import pandas as pd
import json
from api import db, ma
from flask import Response
from api.models.Fish import Fish
from api.schemas.FishSchema import FishSchema


fishes_schema = FishSchema(many=True)


def upload(data):
    for fish in data:
        fish = Fish(
            diagonal_length=fish.get("diagonal_length", None),
            horizontal_length=fish.get("horizontal_length", None),
            vertical_length=fish.get("vertical_length", None),
            height=fish.get("height", None),
            width=fish.get("width", None),
            species=fish.get("species", None),
        )
        db.session.add(fish)
    db.session.commit()
    return Response("Ok", 200)


def uploadFile(file):
    file_extension = file.filename.split(".")[1]
    fishes = []
    s = db.session()
    engine = s.get_bind()
    if file_extension == "xlsx":
        fishes = pd.read_excel(file.read(), engine="openpyxl")
        fishes.to_sql(
            "fishes", con=engine, if_exists="append", chunksize=1000, index=False
        )
        return Response("Upload Successfully", 200)
    elif file_extension == "xls":
        fishes = pd.read_excel(file.read())
        fishes.to_sql(
            "fishes", con=engine, if_exists="append", chunksize=1000, index=False
        )
        return Response("Upload Successfully", 200)
    elif file_extension == "csv":
        fishes = pd.read_csv(file.read())
        fishes.to_sql(
            "fishes", con=engine, if_exists="append", chunksize=1000, index=False
        )
        return Response("Upload Successfully", 200)

    return Response("Error Uploading", 401)



def search(species):
    
    all_Fishes = fishes_schema.dump(Fish.query.filter_by(species=species.lower()).all())
    return {"fishes": all_Fishes}
