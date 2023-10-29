from scipy import stats, spatial
from functools import partial
import pandas as pd
import numpy as np
import random


class KNN:

    def __init__(self, vizinhos=1, metodo="media"):
        # Armazena a quantidade de "prototipos"
        self._vizinhos = vizinhos if vizinhos >= 1 else 1
        self._dict_metodos = dict({
            "media": partial(self._media),
            "mediana": partial(self._mediana),
            "moda": partial(self._moda),
            "media_harmonica": partial(self._media_harmonica),
            "media_min_max": partial(self._media_min_max),
            "aleatorio": partial(self._aleatorio)
        })  # Armazena os tipos e os metodos para achar o "protipo"
        # Armazerna qual metodo para achar prototipo usar
        self._metodo = metodo if metodo in self._dict_metodos.keys() else "media"
        self._prototipos = dict({})  # Armazena os prototipos
        self._dict_individuos = dict({})  # Armazena os individuos

    # Calcula distância Euclidiana
    def _distancia_euclidiana(self, individuo_A, individuo_B):
        return spatial.distance.euclidean(individuo_A, individuo_B)

    def _media(self, matriz):  # Calcula a média
        return np.mean(matriz, axis=0)

    def _mediana(self, matriz):  # Calcula a mediana
        return np.median(matriz, axis=0)

    def _moda(self, matriz):  # Calcula a moda
        return stats.mode(matriz, axis=0)

    def _media_harmonica(self, matriz):  # Calcula a média harmonica
        return stats.hmean(matriz, axis=0)

    # Calcula a média usando os valores min e max de cada atributo
    def _media_min_max(self, matriz):
        matriz_min = np.min(matriz, axis=0)
        matriz_max = np.max(matriz, axis=0)
        matriz_min_max = np.array([matriz_min, matriz_max])
        return np.mean(matriz_min_max, axis=0)

    def _aleatorio(self, matriz):  # Escolhe alguem para ser o prototipo
        return random.choice(matriz)

    def treinamento(self, X_treino, Y_treino):  # Realiza o treinamento
        lista_atributos = X_treino.columns  # Pega as colunas de atributos
        Y_treino.rename("Resultados", inplace=True)  # Muda o nome da coluna
        dados = pd.concat([X_treino, Y_treino], axis=1)  # Junta os dados
        # Cria um dicionário, no qual a chave será, o conjunto, e o valor uma lista com os individuos desse conjunto
        self._dict_individuos = dict({grupo[0]: np.array(
            grupo[1][lista_atributos].values.tolist()) for grupo in dados.groupby(by="Resultados")})
        for grupo in self._dict_individuos.keys():  # For para criar os prototipos
            # Cria um prototipo ficticio, usando o metodo escolhido
            prototipo_ficticio = self._dict_metodos[self._metodo](
                self._dict_individuos[grupo])
            lista_individuos = self._dict_individuos[grupo].copy()
            for individuo in lista_individuos:
                # Calcula a distância euclidiana, entre prototipo ficticio, para todos os individuos do conjunto
                list(individuo).append(self._distancia_euclidiana(
                    prototipo_ficticio, individuo))
            self._prototipos.update(dict(
                {grupo: lista_individuos[lista_individuos[:, -1].argsort()][:self._vizinhos]}))  # Salva os protipos

    def predicao(self, X_teste):  # Realiza a predição
        resultados = []
        for individuo in X_teste.values.tolist():  # Percorre os individuos que devem ser preditos
            resultado_preliminar = dict({})
            for grupo in self._prototipos.keys():
                resultado_preliminar.update(dict({grupo: []}))
                for prototipo in self._prototipos[grupo]:
                    # Calcula a distância euclidiana entre os prototipos para os individuos
                    resultado_preliminar[grupo].append(
                        self._distancia_euclidiana(prototipo, individuo))
                # Pego a menor distância encontrada para o conjunto
                resultado_preliminar[grupo] = min(resultado_preliminar[grupo])
            # Pego qual conjunto foi menor
            resultados.append(
                min(resultado_preliminar, key=resultado_preliminar.get))
        return resultados

    @property
    def prototipos(self):  # Imprimi os prototipos de cada conjunto
        for grupo in self._prototipos.keys():
            print("Os prototipos do grupo " + str(grupo) + " são:")
            for individuo in self._prototipos[grupo]:
                print(" - " + str(individuo))
