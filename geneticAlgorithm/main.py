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

import geneticAlgorithm as GA

generations = 5
# calculate the fitness of the first generation
chromosomes = GA.calculateFitnessOfAllChromosomes(
    GA.getFirstGeneration())
print(chromosomes)

generationNumber = 1
while (generationNumber <= generations):
    # by tournament selection we choose two chromosomes
    firstSelected = GA.selectionByTournment(
        chromosomes)
    secondSelected = GA.selectionByTournment(
        chromosomes)
    
    # crossing them over and calculating their fitness
    crossoveredChromosomes = GA.crossover(firstSelected, secondSelected)
    crossoveredChromosomes = GA.calculateFitnessOfAllChromosomes(
        crossoveredChromosomes)

    # appling mutation to the chromosomes
    for chromosome in crossoveredChromosomes:
        chromosomes.append(GA.mutation(chromosome))
    chromosomes = GA.calculateFitnessOfAllChromosomes(chromosomes)
    GA.printGeneration(chromosomes, generationNumber)
    generationNumber += 1
