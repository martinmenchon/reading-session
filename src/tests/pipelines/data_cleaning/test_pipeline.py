import pandas as pd


def test_data_columns():
    df = pd.read_csv("data/02_intermediate/data_cleaned.csv")
    assert list(df.columns) == ["date", "y"]


def test_train_data_range():
    df = pd.read_csv("data/02_intermediate/data_cleaned.csv")
    df = df.set_index("date")
    df = df.asfreq("MS")
    df = df.sort_index()
    assert (df.index == pd.date_range(start=df.index.min(), end=df.index.max(), freq=df.index.freq)).all() == True
