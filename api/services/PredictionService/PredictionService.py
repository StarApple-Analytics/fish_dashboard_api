import pandas as pd
import pickle
import json

from api.utils import numpyencoder
from api.constant import MODEL_PATH


def predict(width, height, diagLength, horizonLength, verticalLength):

    input_df = cleanData(width, height, diagLength, horizonLength, verticalLength)
    output_df = predict_weight(input_df)


    return {
        "weight": output_df[0],
    }


def cleanData(width, height, diagLength, horizonLength, verticalLength):
    return pd.DataFrame(
        [[width, height, diagLength, horizonLength, verticalLength]],
        columns=["VerLength", "DiagLength", "HorizonLength", "Height", "Width"],
    )


def predict_weight(input_df):

    model = pickle.load(open(MODEL_PATH, "rb"))

    output_df = model.predict(input_df)
    return output_df
