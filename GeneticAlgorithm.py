from random import randrange
from math import sin, sqrt
from copy import deepcopy
from MathFunctions import stdDev, sigma

STEP = 50  # percent
direction = 1

# max = 231.7211106994124
# max_a = 20.47
# max_b = 20.47


def fitness(a, b):
    return ((a / 2) * sin(a) + 5) * ((b / 2) * sin(b) + 5)


def diversity(chromosome, avg_chromosome):
    d_sum = 0
    for index in range(len(chromosome)):
        d_sum += abs(avg_chromosome[index]-chromosome[index])
    return (sigma(d_sum/(len(chromosome)*10)))*232


def fdValues(population):
    avg_chrm = [sum([population[i][index] for i in range(len(population))]) / len(population) for index in range(len(population[0]))]

    f_values = [fitness(population[i][0], population[i][1]) for i in range(len(population))]
    d_values = [diversity(population[i], avg_chrm) for i in range(len(population))]

    return list(zip(population, f_values, d_values))


def retrieveKeptChromosomes(population):
    fd_values = fdValues(population)

    return_chromosomes = []
    rs = []
    for tup in fd_values:
        rs.append(sqrt(((232-tup[1])**2) + ((232-tup[2])**2)))
    r_values = list(sorted(zip(rs, [fd_values[i][0] for i in range(len(fd_values))])))
    for tup in r_values[:250]:
        return_chromosomes.append(tup[1])

    return return_chromosomes


def mutateChromosome(chromosome, mutations_per_chromosome):
    new_chromosome = chromosome
    global direction

    for _ in range(mutations_per_chromosome):
        direction = direction - 2*direction
        percent = (randrange(STEP // 2, STEP) / 100) * direction
        new_chromosome[randrange(0,len(new_chromosome))] *= percent

    return new_chromosome


def printStats(population):
    avg_chrm = [sum([population[i][0] for i in range(len(population))]) / len(population),
                sum([population[i][1] for i in range(len(population))]) / len(population)
                ]
    print('Mean Chromosome: ', avg_chrm)

    max, max_i = 0, 0
    for i, c in enumerate(population):
        c_f = fitness(c[0], c[1])
        if max < c_f: max, max_i  = c_f, i
    print('Highest Fitness: ', max, '--', population[max_i])

    max, max_i = 0, 0
    for i, c in enumerate(population):
        c_f = diversity(c, avg_chrm)
        if max < c_f: max, max_i = c_f, i
    print('Highest Diversity: ', max, '--', population[max_i])

    if __name__ == '__main__':
        total_f = 0
        for c in population:
            total_f += fitness(c[0], c[1])
        print('Mean Fitness: ', total_f/len(population))

    total_d = 0
    for c in population:
        total_d += diversity(c, avg_chrm)
    print('Mean Diversity: ', total_d / len(population))

    stddev_sum = 0
    pop_size = len(population[0])
    for index in range(pop_size):
        stddev_sum += stdDev([population[i][index] for i in range(len(population))])
    avg_stddev = stddev_sum/pop_size
    print('Standard Deviation: ', avg_stddev)

if __name__ == '__main__':
    chromosomes = [[3, 3] for _ in range(500)]
    close = False
    generation = 1

    while not close:
        command = input("Enter command or how many generations to simulate.  \n\n    > ")
        try:
            generations = int(command)

            for g in range(generations):
                print('Generation:', generation+g)

                chromosomes = retrieveKeptChromosomes(chromosomes)

                for index in range(250):
                    chrsm = mutateChromosome(deepcopy(chromosomes[index]), 5)
                    for i, x in enumerate(chrsm):
                        if x > 25: chrsm[i] = 25.0
                        if x < 0: chrsm[i] = 0.0

                    chromosomes.append(chrsm)

                for _ in range(randrange(50, 75)):
                    chr_1_i, chr_2_i = 0, 0
                    while chr_1_i == chr_2_i:
                        chr_1_i = randrange(0, 500)
                        chr_2_i = randrange(0, 500)
                    chr_1 = chromosomes[chr_1_i]
                    chr_2 = chromosomes[chr_2_i]
                    chromosomes[chr_1_i] = chr_1[:1] + chr_2[1:]
                    chromosomes[chr_2_i] = chr_2[:1] + chr_1[1:]

            generation += generations

        except ValueError:
            if command == 'stop': close = True
            elif command == 'stats': printStats(chromosomes)
            elif command == 'step':
                try: STEP = int(input("    New STEP Value -- "))
                except:
                    print('ERROR: STEP Not Int')
                    print('    STEP Reverted to Previous STEP:', STEP)
            elif command == 'population':
                for index, chromosome in enumerate(chromosomes):
                    if (index % 50) == 0: input()
                    print('Chromosome', index+1, '--', chromosome)
            elif command == 'help':
                print('Commands:\n  stop\n  stats\n  step\n  population\n  help')
            else: print('Incorrect Command')
