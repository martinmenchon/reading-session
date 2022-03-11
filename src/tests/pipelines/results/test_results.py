import pandas as pd


def test_forecasting_not_empty():
    df = pd.read_csv("data/07_model_output/y_pred.csv")
    assert df.empty is False
