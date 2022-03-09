import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')
plt.rcParams['lines.linewidth'] = 1.5

def train_test_split(data, steps):
    data_train = data[:-steps]
    y_true = data[-steps:]

    fig, ax = plt.subplots(figsize=(9, 4))
    data_train['y'].plot(ax=ax, label='train')
    y_true['y'].plot(ax=ax, label='test')
    ax.legend()
    plt.savefig("./data/02_intermediate/plot.jpg")
    return data_train, y_true
