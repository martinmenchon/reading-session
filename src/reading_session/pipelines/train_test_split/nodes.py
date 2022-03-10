def train_test_split(data, steps):
    data_train = data[:-steps]
    y_true = data[-steps:]

    return data_train, y_true
