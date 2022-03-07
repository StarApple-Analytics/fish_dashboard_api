import pandas as pd

from flask import jsonify

from string import punctuation
from collections import Counter

from api.models.Fish import Fish
from api.schemas.FishSchema import FishSchema



fish_schema = FishSchema()
fishes_schema = FishSchema(many=True)


def dashboardData():

    all_Fishes = fishes_schema.dump(Fish.query.all())

    unique_Species = list(Counter([fish["species"] for fish in all_Fishes]).items())
    total_weight =sum(fish["weight"] for fish in all_Fishes)
    average_weight = total_weight/len(all_Fishes)
    
    
    fish_height_data_directory = {}

    for fish in all_Fishes:
        fish_height_data_directory[fish["species"]] = fish_height_data_directory.get(fish["species"], []) + [fish["height"]]

    fish_heights = []
    
    for key, value in fish_height_data_directory.items():
        avg_height = sum(value) / len(value)
        max_height = max(value)

        fish_heights.append({
            "species": key,
            "avg_height": avg_height,
            "max_height": max_height
        })
    

    fish_width_data_directory = {}

    for fish in all_Fishes:
        fish_width_data_directory[fish["species"]] = fish_width_data_directory.get(fish["species"], []) + [fish["width"]]

    fish_widths = []
    
    for key, value in fish_width_data_directory.items():
        avg_width = sum(value) / len(value)
        max_width = max(value)

        fish_widths.append({
            "species": key,
            "avg_width": avg_width,
            "max_width": max_width
        })
    

    fish_length_data_directory = {}

    for fish in all_Fishes:
        fish_length_data_directory[fish["species"]] = fish_length_data_directory.get(fish["species"], []) + [fish["length"]]

    fish_lengths = []
    
    for key, value in fish_length_data_directory.items():
        avg_length = sum(value) / len(value)
        max_length = max(value)

        fish_lengths.append({
            "species": key,
            "avg_length": avg_length,
            "max_length": max_length
        })



    return {
        "total_unique_fishes": len(unique_Species),
        "total_weight": total_weight,
        "total_fishes": len(all_Fishes),
        "average_weight": average_weight,
        "unique_fishes": unique_Species,
        "fishes_heights": fish_heights,
        "fishes_widths": fish_widths,
        "fishes_lengths": fish_lengths,
        "fishes": all_Fishes,
    }

