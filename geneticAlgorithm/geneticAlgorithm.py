"""
Authors: Érick de Castro Silva, Luiz Fernando Ferreira Santos

Função: x^2 - 3x + 4, encontre o valor máximo.

- Assumir que x [-10, +10].
- Codificar X como vetor binário.
- Criar uma população inicial com 4  indivíduos.
- Aplicar Mutação com taxa de 1%.
- Aplicar Crossover com taxa de 70%.
- Usar seleção por torneio.
- Usar 5  gerações.

"""

import random

crossoverTax = 0.7
mutation = 0.1


def fitness(x):
    return x*x - 3 * x + 4


def calculateFitnessOfAllChromosomes(chromosomes):
    i = 0
    for chromoso in chromosomes:
        # separate sign from value
        splitChromoso = chromoso[0].split()
        chromosoSign = splitChromoso[0]
        chromosoValue = splitChromoso[1]

        # chromoso at 1 receives its fitness
        chromoso[1] = fitness(int(chromosoSign + chromosoValue, 2))
        chromosomes[i] = chromoso
        i += 1
    return chromosomes


def selectionByTournment(chromosomes):
    twoSelected = [[], []]
    max = 0
    secondMax = 0
    if (chromosomes[0][1] >= chromosomes[1][1]):
        max = chromosomes[0]
        secondMax = chromosomes[1]
    else:
        max = chromosomes[1]
        secondMax = chromosomes[0]
    for i in range(2, len(chromosomes), 1):
        if (chromosomes[i][1] > max[1]):
            secondMax = max
            max = chromosomes[i]
        elif (chromosomes[i][1] > secondMax[1]):
            secondMax = chromosomes[i]
    twoSelected[0] = max
    twoSelected[1] = secondMax
    return twoSelected


def crossover(chromosomeA, chromosomeB):
    # getting sign and value from chromosomes
    signAndValueArrayA = chromosomeA[0].split()
    signAndValueArrayB = chromosomeB[0].split()

    # setting crossOverPoint and getting chromosomes' "tails"
    crossOverPoint = int(len(signAndValueArrayA[1]) * crossoverTax)
    chromosomeATail = signAndValueArrayA[1][crossOverPoint:]
    chromosomeBTail = signAndValueArrayB[1][crossOverPoint:]

    # crossing over
    signAndValueArrayA[1] = signAndValueArrayA[:crossOverPoint] + \
        chromosomeBTail
    signAndValueArrayB[1] = signAndValueArrayB[:crossOverPoint] + \
        chromosomeATail

    chromosomeA[0] = signAndValueArrayA[0] + ' ' + signAndValueArrayA[1]
    chromosomeB[0] = signAndValueArrayA[0] + ' ' + signAndValueArrayA[1]
    return chromosomeA, chromosomeB


def mutation(chromosome):
    genesQuantity = len(chromosome)
    randomGene = random.randint(0, genesQuantity - 1)
    chromosome[randomGene] = not chromosome[randomGene]
    return chromosome
