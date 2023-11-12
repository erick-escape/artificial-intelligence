from sklearn import datasets
import pandas as pd
import kmeans as kmeans
import visualization as visualization

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df["classe"] = iris.target
iris_df.columns = ['sepal_len', 'sepal_wid',
                   'petal_len', 'petal_wid', 'classe']

iris_df.tail()
iris_df.describe()
irisData = iris_df.drop("classe", axis=1).values.tolist()

centroids = kmeans.startCentroids()
print("CENTROIDS: ", centroids)

irisClusterization, centroids = kmeans.kmeans(centroids, irisData)

# Sepal Lenght vs Sepal Width
visualization.plotResult(0, 1, 'Sepal Lenght (cm)', 'Sepal Width (cm)',
                         'Sepal Lenght vs Sepal Width', 'upper right',
                         irisClusterization, centroids, iris)

# Sepal Lenght vs Petal Width
visualization.plotResult(0, 3, 'Sepal Length (cm)', 'Petal Width (cm)',
                         'Sepal Length vs Petal Width', 'lower right',
                         irisClusterization, centroids, iris)

# Sepal Width vs Petal Width
visualization.plotResult(1, 3, 'Sepal Width (cm)', 'Petal Width (cm)',
                         'Sepal Width vs Sepal Width', 'center right',
                         irisClusterization, centroids, iris)

# Petal Lenght vs Sepal Lenght
visualization.plotResult(2, 0, 'Petal Length (cm)', 'Sepal Lenght (cm)',
                         'Petal Length vs Sepal Lenght', 'lower right',
                         irisClusterization, centroids, iris)

# Petal Length vs Sepal Width
visualization.plotResult(2, 1, 'Petal Length (cm)', 'Sepal Width (cm)',
                         'Petal Length vs Sepal Width', 'upper right',
                         irisClusterization, centroids, iris)

# Petal Lenght vs Petal Width
visualization.plotResult(2, 3, 'Petal Length (cm)', 'Petal Width (cm)',
                         'Petal Length vs Petal Width', 'lower right',
                         irisClusterization, centroids, iris)
