# import required libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from hmmlearn import hmm
from sklearn.model_selection import train_test_split


# load and preprocess data
data = pd.read_csv("data.csv")
X = data.drop(["target"], axis=1)
y = data["target"]

# split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# create and train linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# create and train neural network model
mlp = MLPRegressor(hidden_layer_sizes=(10, 5), max_iter=1000)
nn = MLPRegressor(hidden_layer_sizes=(10,), activation='relu')
nn.fit(X_train, y_train)

# create and train random forest model
rf = RandomForestRegressor(n_estimators=100)
rf.fit(X_train, y_train)

# create and train Hidden Markov Model
hmm_model = hmm.GaussianHMM(n_components=4)
hmm_model.fit(X_train)

# evaluate models on test data
lr_score = lr.score(X_test, y_test)
nn_score = nn.score(X_test, y_test)
rf_score = rf.score(X_test, y_test)
hmm_score = hmm_model.score(X_test)

# choose best model and make prediction
models = {'lr': lr_score, 'nn': nn_score, 'rf': rf_score, 'hmm': hmm_score}
best_model = max(models, key=models.get)

if best_model == 'lr':
    prediction = lr.predict(X_test)
elif best_model == 'nn':
    prediction = nn.predict(X_test)
elif best_model == 'rf':
    prediction = rf.predict(X_test)
else:
    prediction = hmm_model.predict(X_test)

# print prediction and model used
print(f"Prediction: {prediction}")
print(f"Best model: {best_model}")




