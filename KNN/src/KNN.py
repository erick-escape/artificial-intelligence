from scipy import stats, spatial
from functools import partial
import pandas as pd
import numpy as np
import random


class KNN:
    def __init__(self, neighbors=1, method="mean"):
        self._neighbors = neighbors if neighbors >= 1 else 1
        self._dict_methods = dict({
            "mean": partial(self._mean),
            "median": partial(self._median),
            "mode": partial(self._mode),
            "harmonic_mean": partial(self._harmonic_mean),
            "mean_min_max": partial(self._mean_min_max),
            "random": partial(self._random)
        })
        self._method = method if method in self._dict_methods.keys() else "mean"
        self._prototypes = dict({})
        self._dict_individuals = dict({})

    def _euclidean_distance(self, A, B):
        return spatial.distance.euclidean(A, B)

    def _mean(self, matrix):
        return np.mean(matrix, axis=0)

    def _median(self, matrix):
        return np.median(matrix, axis=0)

    def _mode(self, matrix):
        return stats.mode(matrix, axis=0)

    def _harmonic_mean(self, matrix):
        return stats.hmean(matrix, axis=0)

    def _mean_min_max(self, matrix):
        matrix_min = np.min(matrix, axis=0)
        matrix_max = np.max(matrix, axis=0)
        matrix_min_max = np.array([matrix_min, matrix_max])
        return np.mean(matrix_min_max, axis=0)

    def _random(self, matrix):  # Makes a random choice to get the prototype
        return random.choice(matrix)

    def training(self, X_training, Y_training):
        attributes = X_training.columns
        Y_training.rename("results", inplace=True)
        data = pd.concat([X_training, Y_training], axis=1)
        # Makes a dictionary, in which the key will be the set and the value a list with this sets individuals
        self._dict_individuals = dict({group[0]: np.array(
            group[1][attributes].values.tolist()) for group in data.groupby(by="results")})
        for group in self._dict_individuals.keys():  # For to create the prototypes
            fictitious_prototype = self._dict_methods[self._method](
                self._dict_individuals[group])
            individuals = self._dict_individuals[group].copy()
            for individual in individuals:
                # Calculates the euclidean distance between fictitious prototype and all the sets individuals
                list(individual).append(self._euclidean_distance(
                    fictitious_prototype, individual))
            self._prototypes.update(dict(
                {group: individuals[individuals[:, -1].argsort()][:self._neighbors]}))

    def prediction(self, X_test):
        results = []
        for individual in X_test.values.tolist():  # Individuals to be predicted
            partial_result = dict({})
            for group in self._prototypes.keys():
                partial_result.update(dict({group: []}))
                for prototype in self._prototypes[group]:
                    # Calculates the euclidean distance between prototypes and individuals
                    partial_result[group].append(
                        self._euclidean_distance(prototype, individual))
                # Gets the smallest distance encountered for the set
                partial_result[group] = min(partial_result[group])
            # Gets the smallest set
            results.append(
                min(partial_result, key=partial_result.get))
        return results

    @property
    def prototypes(self):  # Print the set prototypes
        for set in self._prototypes.keys():
            print("Sets prototypes " + str(set) + ":")
            for individual in self._prototypes[set]:
                print(" - " + str(individual))
