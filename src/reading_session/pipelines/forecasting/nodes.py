from sklearn.ensemble import RandomForestRegressor
from skforecast.ForecasterAutoreg import ForecasterAutoreg


def run_forecasting(data_train, steps, lags):
    forecaster = ForecasterAutoreg(
        regressor=RandomForestRegressor(random_state=123),
        lags=lags
    )

    forecaster.fit(y=data_train['y'])
    forecaster
    y_pred = forecaster.predict(steps=steps)
    return y_pred
