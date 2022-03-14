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
    total_weight = sum(fish["weight"] for fish in all_Fishes)
    average_weight = total_weight / len(all_Fishes)

    fish_height_data_directory = {}

    for fish in all_Fishes:
        fish_height_data_directory[fish["species"]] = fish_height_data_directory.get(
            fish["species"], []
        ) + [fish["height"]]

    fish_heights = []

    for key, value in fish_height_data_directory.items():
        avg_height = sum(value) / len(value)
        max_height = max(value)

        fish_heights.append(
            {"species": key, "avg_height": avg_height, "max_height": max_height}
        )

    fish_width_data_directory = {}

    for fish in all_Fishes:
        fish_width_data_directory[fish["species"]] = fish_width_data_directory.get(
            fish["species"], []
        ) + [fish["width"]]

    fish_widths = []

    for key, value in fish_width_data_directory.items():
        avg_width = sum(value) / len(value)
        max_width = max(value)

        fish_widths.append(
            {"species": key, "avg_width": avg_width, "max_width": max_width}
        )

    fish_diagonal_length_data_directory = {}

    for fish in all_Fishes:
        fish_diagonal_length_data_directory[
            fish["species"]
        ] = fish_diagonal_length_data_directory.get(fish["species"], []) + [
            fish["diagonal_length"]
        ]

    fish_diagonal_lengths = []

    for key, value in fish_diagonal_length_data_directory.items():
        avg_diagonal_length = sum(value) / len(value)
        max_diagonal_length = max(value)

        fish_diagonal_lengths.append(
            {
                "species": key,
                "avg_diagonal_length": avg_diagonal_length,
                "max_diagonal_length": max_diagonal_length,
            }
        )

    fish_vertical_length_data_directory = {}

    for fish in all_Fishes:
        fish_vertical_length_data_directory[
            fish["species"]
        ] = fish_vertical_length_data_directory.get(fish["species"], []) + [
            fish["vertical_length"]
        ]

    fish_vertical_lengths = []

    for key, value in fish_vertical_length_data_directory.items():
        avg_vertical_length = sum(value) / len(value)
        max_vertical_length = max(value)

        fish_vertical_lengths.append(
            {
                "species": key,
                "avg_vertical_length": avg_vertical_length,
                "max_vertical_length": max_vertical_length,
            }
        )

    fish_horizontal_length_data_directory = {}

    for fish in all_Fishes:
        fish_horizontal_length_data_directory[
            fish["species"]
        ] = fish_vertical_length_data_directory.get(fish["species"], []) + [
            fish["horizontal_length"]
        ]

    fish_horizontal_lengths = []

    for key, value in fish_horizontal_length_data_directory.items():
        avg_horizontal_length = sum(value) / len(value)
        max_horizontal_length = max(value)

        fish_horizontal_lengths.append(
            {
                "species": key,
                "avg_horizontal_length": avg_horizontal_length,
                "max_horizontal_length": max_horizontal_length,
            }
        )     
    return {
        "total_unique_fishes": len(unique_Species),
        "total_weight": total_weight,
        "total_fishes": len(all_Fishes),
        "average_weight": average_weight,
        "unique_fishes": unique_Species,
        "fishes_heights": fish_heights,
        "fishes_widths": fish_widths,
        "fishes_diagonal_lengths": fish_diagonal_lengths,
        "fishes_vertical_lengths": fish_vertical_lengths,
        "fishes_horizontal_lengths": fish_horizontal_lengths,
        "fishes": all_Fishes,
    }
