from time import sleep

import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor


class RegressionModel():
    def __int__(self, path):
        self.path = path

    def start_predictions(self, path='./ml/melb_data.csv'):
        X, y = self.read_data(path)
        result = self.build_model(X, y)
        sleep(2)
        return result

    def read_data(self, path):
        big_data = pd.read_csv(path)
        big_data = big_data.dropna(axis=0)
        X, y = self.choosing_target_and_features(big_data)
        return X, y

    def choosing_target_and_features(self, big_data):
        y = big_data.Price # target
        data_features = [
            'Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'
            ] # features
        X = big_data[data_features]
        return  X, y

    def build_model(self, X, y):
        model = DecisionTreeRegressor(random_state=1)
        model.fit(X, y)
        predicted = model.predict(X)
        result = mean_absolute_error(y, predicted)
        return result

def main():
    do_something()

if __name__ == '__main__':
    model = RegressionModel()
    model.start_predictions(model_id)
