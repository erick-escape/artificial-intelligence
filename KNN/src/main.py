from KNN import KNN
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics

knn = KNN(vizinhos=1)
dataset = pd.read_csv("../data/iris.csv")
print(dataset)
