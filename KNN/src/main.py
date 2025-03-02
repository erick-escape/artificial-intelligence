# Authors: Érick de Castro Silva e Luís Fernando Ferreira Santos

from KNN import KNN
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics

knn = KNN(neighbors=1)
dataset = pd.read_csv("../data/iris.csv")
X = dataset.drop(columns=["Id", "Species"])
Y = dataset["Species"]

X_training, X_test, Y_training, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=7)

# TESTS

method = "median"
print("METHOD: ", method)
for i in range(1, 7, 2):
    print("NEIGHBORS: ", i, "\n")
    knn = KNN(neighbors=i, method=method)
    knn.training(X_training, Y_training)
    print("\nPROTOTYPES:\n")
    knn.prototypes
    result = knn.prediction(X_test)
    print("\nMETRICS:\n")
    print(metrics.classification_report(Y_test, result, digits=3), "\n")
