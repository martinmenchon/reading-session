import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


def results(data_train, y_true, y_pred):
    fig, ax = plt.subplots(figsize=(9, 4))
    data_train["y"].plot(ax=ax, label="train")
    y_true["y"].plot(ax=ax, label="test")
    y_pred.plot(ax=ax, label="y_pred")
    ax.legend()
    plt.savefig("./data/07_model_output/results.jpg")

    error_mse = mean_squared_error(y_true=y_true["y"], y_pred=y_pred)
    print(f"Error de test (mse): {error_mse}")
    y_true["y"] = y_pred
    return y_true
