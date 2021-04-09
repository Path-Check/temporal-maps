from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, mean_squared_error, accuracy_score


class Models:
    def __init__(self, data, logger, categorical, continious):

        self.categorical = categorical
        self.continious = continious
        self.data = data
        self.logger = logger

    def fit(self, name, classifier=None, regressor=None):

        classifier_results = {}
        regressor_results = {}

        if classifier:

            for feature in self.categorical:
                data = self.data
                data_y = data[feature]
                data_x = data.drop(columns=[feature])
                X_train, X_test, y_train, y_test = train_test_split(
                    data_x, data_y, test_size=0.33, random_state=42
                )
                classifier.fit(data_x, data_y)
                print("\n")
                print(feature)
                print("\n")
                print(classification_report(classifier.predict(X_test), y_test))
                print("\n")
                accuracy = accuracy_score(classifier.predict(X_test), y_test)
                classifier_results[feature] = accuracy

        if regressor:

            for feature in self.continious:
                data_y = data[feature]
                data_x = data.drop(columns=[feature])
                X_train, X_test, y_train, y_test = train_test_split(
                    data_x, data_y, test_size=0.33, random_state=42
                )
                regressor.fit(data_x, data_y)
                print("\n")
                print(feature)
                print("\n")
                accuracy = mean_squared_error(regressor.predict(X_test), y_test)
                print(accuracy)
                print("\n")
                regressor_results[feature] = accuracy

        accuracy_scores = {**classifier_results, **regressor_results}
        print(accuracy_scores)
        self.logger[name] = accuracy_scores

    def evaluate(self):

        pass
