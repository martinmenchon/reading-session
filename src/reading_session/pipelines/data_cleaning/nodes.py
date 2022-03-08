import pandas as pd


def data_cleaning(data):
    data_cleaned = data[['date', 'y']]
    data_cleaned['date'] = pd.to_datetime(data_cleaned['date'], format='%Y/%m/%d')
    data_cleaned = data_cleaned.set_index('date')
    data_cleaned = data_cleaned.asfreq('MS')
    data_cleaned = data_cleaned.sort_index()
    (data_cleaned.index == pd.date_range(
        start=data_cleaned.index.min(),
        end=data_cleaned.index.max(),
        freq=data_cleaned.index.freq)
     ).all()
    return data_cleaned