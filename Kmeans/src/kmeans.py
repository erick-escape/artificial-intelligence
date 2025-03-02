from scipy.spatial import distance
import numpy as np

k = 3  # Clusters
numberOfColumns = 4  # Columns in data set
inferiorLimit = [4, 2, 1, 0]
superiorLimit = [8, 5, 7, 3]
convergenceLimit = 0.02
maxIterations = 100

def startCentroids():
    centroids = np.random.uniform(
        inferiorLimit, superiorLimit, (k, numberOfColumns))
    return np.round(centroids, 2).tolist()

def euclideanDistance(p1, p2):
    return distance.euclidean(p1, p2)

def getMidPoint(points):
    if len(points) == 0:
        return [0.0] * numberOfColumns  # origin

    dimensions = len(points[0])
    midPoint = [0.0] * dimensions

    for point in points:
        for dimension in range(dimensions):
            midPoint[dimension] += point[dimension]

    for dimension in range(dimensions):
        midPoint[dimension] /= len(points)

    return midPoint

def centroidsRepositioning(cluster, centroids):
    newCentroids = []
    for centroid in centroids:
        points = cluster[centroids.index(centroid)]
        if len(points) != 0:
            newCentroid = getMidPoint(points)
        else:
            newCentroid = centroid
        newCentroids.append(newCentroid)
    return newCentroids

def verifyConvergence(oldPoints, currentPoints):
    for oldPoint, currentPoint in zip(oldPoints, currentPoints):
        if euclideanDistance(oldPoint, currentPoint) > convergenceLimit:
            return True
    return False

def nearestCentroid(point, centroids):
    nearestCentroid = -1
    minDistance = 999999

    for i in range(0, k):
        distance = euclideanDistance(point, centroids[i])
        if distance < minDistance:
            minDistance = distance
            nearestCentroid = i
    return nearestCentroid

def initializeEmptyClusters():
    cluster = []
    for i in range(k):
        cluster.append(list())
    return cluster


def kmeans(centroids, points):
    clusters = []  # Matrix -> cluster x itens x coordenadas
    count = 0  # iterations count
    newCentroids = []

    while count < maxIterations and (count == 0 or verifyConvergence(centroids, newCentroids)):
        clusters = initializeEmptyClusters()
        if count != 0:
            centroids = newCentroids
        for point in points:
            pos = nearestCentroid(point, centroids)
            clusters[pos].append(point)
        count += 1
        newCentroids = centroidsRepositioning(
            clusters, centroids)

    return clusters, centroids
