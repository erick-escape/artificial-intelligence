import random

genes = 4
chromosomes = 4
crossoverRate = 70
mutationRate = 1
crossoverPoint = 2

def decimalToTwosComplement(decimal, bits=5):
    if decimal >= 0:
        binary = bin(decimal)[2:].zfill(bits)
    else:
        abs_decimal = abs(decimal)
        oneComplement = bin(abs_decimal - 1)[2:]
        twosComplement = ''.join('1' if bit == '0' else '0' for bit in oneComplement.zfill(bits))
        binary = twosComplement

    return binary

def twosComplementToDecimal(binary):
    if binary[0] == '1':
        oneComplement = ''.join('1' if bit == '0' else '0' for bit in binary)
        twosComplement = bin(int(oneComplement, 2) + 1)[2:]
        decimal = -int(twosComplement, 2)
        return decimal
    else:
        decimal = int(binary, 2)
        return decimal

def getFirstGeneration():
    generation = []
    for i in range(0, chromosomes, 1):
        generation.append([decimalToTwosComplement(random.randint(-10, 10)), 0])
    return generation

def fitness(x):
    return x*x - 3 * x + 4

def calculateFitnessOfAllChromosomes(chromosomes):
    for chromosome in chromosomes:
        # getting decimal to calculate fitness
        decimal = twosComplementToDecimal(chromosome[0])

        # chromoso at 1 receives its fitness
        chromosome[1] = fitness(decimal)
    return chromosomes

def selectionByTournment(chromosomes):
    randomChromosomeA = random.randint(0, len(chromosomes) - 1)
    randomChromosomeB = random.randint(0, len(chromosomes) - 1)
    if (chromosomes[randomChromosomeA][1] > chromosomes[randomChromosomeB][1]):
        winnerChromosome = chromosomes[randomChromosomeA]
        del chromosomes[randomChromosomeA]
    else:
        winnerChromosome = chromosomes[randomChromosomeB]
        del chromosomes[randomChromosomeB]
    return winnerChromosome

def crossover(chromosomeA, chromosomeB):
    randomInteger = random.randint(1, 100)
    if (randomInteger <= crossoverRate):
        # setting crossoverPoint and getting chromosomes' "tails"
        chromosomeATail = chromosomeA[0][crossoverPoint:]
        chromosomeBTail = chromosomeB[0][crossoverPoint:]

        # crossing over
        if (-10 <= twosComplementToDecimal(chromosomeA[0][:crossoverPoint] + chromosomeBTail) <= 10):
            chromosomeA[0] = chromosomeA[0][:crossoverPoint] + chromosomeBTail
        elif (-10 <= twosComplementToDecimal(chromosomeB[0][:crossoverPoint] + chromosomeATail) <= 10):
            chromosomeB[0] = chromosomeB[0][:crossoverPoint] + chromosomeATail
    return [chromosomeA, chromosomeB]

def mutation(chromosome):
    # getting sign and value from chromosomes
    newValue = ''
    for bit in chromosome[0]:
        randomInteger = random.randint(1, 100)
        if (randomInteger <= mutationRate):
            newValue += str(int(not bit))
        else:
            newValue += str(bit)

    if (-10 <= twosComplementToDecimal(newValue) <= 10):
        chromosome[0] = newValue
    return chromosome

def printGeneration(chromosomes, generationNumber):
    print("\nGeneration: ", generationNumber)
    print("\nChromosomes:\n\n")
    for chromosome in chromosomes:
        print("Chromosome: ", chromosome[0], " - Fitness: ", chromosome[1])
