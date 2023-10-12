import geneticAlgorithm as GA

genes = 4
chromosomes = 4
generations = 5
firstChromosomes = [
    ['+ 0001', 0],
    ['+ 0010', 0],
    ['- 0001', 0],
    ['- 0010', 0],
]


while (generations):
    chromosomesFitnesses = GA.calculateFitnessOfAllChromosomes(
        firstChromosomes)
    selectedChromosomes = GA.selectionByTournment(
        chromosomesFitnesses)
    generations -= 1
