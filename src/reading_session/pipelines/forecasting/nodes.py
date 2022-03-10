import matplotlib.pyplot as plt
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.ensemble import RandomForestRegressor

plt.style.use("fivethirtyeight")
plt.rcParams["lines.linewidth"] = 1.5


def run_forecasting(data_train, steps, lags):
    forecaster = ForecasterAutoreg(regressor=RandomForestRegressor(random_state=123), lags=lags)

    forecaster.fit(y=data_train["y"])
    forecaster
    y_pred = forecaster.predict(steps=steps)
    return y_pred
