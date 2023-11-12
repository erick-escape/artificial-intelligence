from matplotlib import pyplot as plt


def getListThePosition(pos, data):
    lista = list()
    for i in data:
        lista.append(i[pos])
    return lista


def plotResult(position1, position2, xLabel, yLabel, defaultTitle, legendPosition, irisClusterization, centroids, iris):
    plt.figure(figsize=(12, 5))
    plt.subplot(121)

    plt.scatter(getListThePosition(position1, irisClusterization[0]), getListThePosition(
        position2, irisClusterization[0]), s=50, c='green', label='0')
    plt.scatter(getListThePosition(position1, irisClusterization[1]), getListThePosition(
        position2, irisClusterization[1]), s=50, c='orange', label='1')
    plt.scatter(getListThePosition(position1, irisClusterization[2]), getListThePosition(
        position2, irisClusterization[2]), s=50, c='blue', label='2')
    plt.scatter(getListThePosition(position1, centroids), getListThePosition(
        position2, centroids), s=50, c='red', label='Centroids',  marker='^')
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(defaultTitle + ' - with Kmeans')
    plt.legend(loc=legendPosition)

    plt.subplot(122)
    X = iris.data
    y = iris.target

    setosa = X[y == 0]
    versicolor = X[y == 1]
    virginica = X[y == 2]

    plt.scatter(virginica[:, position1], virginica[:,
                position2], label='Virginica',  s=50, c='green')
    plt.scatter(versicolor[:, position1], versicolor[:,
                position2], label='Versicolor', s=50, c='orange')
    plt.scatter(setosa[:, position1], setosa[:, position2],
                label='Setosa', s=50, c='blue')

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(defaultTitle)
    plt.legend(loc=legendPosition)

    plt.show()
