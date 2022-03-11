import pandas as pd


def data_cleaning(data):
    data_cleaned = data[["date", "y"]]
    data_cleaned["date"] = pd.to_datetime(data_cleaned["date"], format="%Y/%m/%d")
    data_cleaned = data_cleaned.set_index("date")
    data_cleaned = data_cleaned.asfreq("MS")
    data_cleaned = data_cleaned.sort_index()

    return data_cleaned
