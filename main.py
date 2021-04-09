import pandas as pd
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, mean_squared_error
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from pytorch_tabnet.tab_model import TabNetClassifier, TabNetRegressor
from xgboost import XGBClassifier, XGBRegressor
from sklearn.metrics import accuracy_score
import numpy as np
from data import Dataset
from model import Models
from utils import Logger

print("[Evaluator]: Beginning Evaluation..........")

logger = Logger()

dataset = Dataset(
    "dataset/dataset.csv", drop_columns=["PUMA", "YEAR", "sim_individual_id"]
)
categorical, continuous = dataset.split_cat_cont()
data = dataset.data
models = Models(data, logger, categorical, continuous)

# Neural Networks
clf = MLPClassifier(
    solver="sgd", alpha=1e-5, hidden_layer_sizes=(30, 30), random_state=1
)
# regr = MLPRegressor(
#   solver="sgd", alpha=1e-6, hidden_layer_sizes=(30, 30), random_state=1
# )
models.fit("MLP", clf)

# Random Forest
clf = RandomForestClassifier(max_depth=3)
# regr = RandomForestRegressor(max_depth=5, random_state=0, n_estimators=400)

models.fit("Random Forest", clf)

# XG Boost
clf = XGBClassifier()
models.fit("XGB Classifier", clf)
# XG Boost Regression

# TabNet
