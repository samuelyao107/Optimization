import random

# Create random chromosomes
def random_chromosome(size):
    return [random.randint(0, size - 1) for _ in range(size)]

# Calculate fitness
def fitness(chromosome, maxFitness):
    horizontal_collisions = (
        sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2
    )
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * (2 * n - 1)
    right_diagonal = [0] * (2 * n - 1)
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter

    # 28 - (2 + 3) = 23
    return int(maxFitness - (horizontal_collisions + diagonal_collisions))

# Crossover between two chromosomes
def crossover(x, y):
    n = len(x)
    child = [0] * n
    for i in range(n):
        c = random.randint(0, 1)
        if c < 0.5:
            child[i] = x[i]
        else:
            child[i] = y[i]
    return child

# Mutation by changing the value of a random index of the chromosome
def mutation(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(0, n - 1)
    x[c] = m
    return x

# Calculate probability
def probability(chromosome, maxFitness):
    return fitness(chromosome, maxFitness) / maxFitness

# Roulette selection
def random_selection(population, probabilities):
    population_with_probability = zip(population, probabilities)
    total = sum(w for c, w in population_with_probability)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"

# Genetic algorithm
def genetic_algorithm(population, maxFitness):
    mutation_probability = 0.1
    new_population = []
    sorted_population = []
    probabilities = []
    for n in population:
        f = fitness(n, maxFitness)
        probabilities.append(f / maxFitness)
        sorted_population.append([f, n])

    sorted_population.sort(reverse=True)

    # Elitism
    new_population.append(sorted_population[0][1])  # best genome
    new_population.append(sorted_population[-1][1])  # worst genome

    for i in range(len(population) - 2):
        chromosome_1 = random_selection(population, probabilities)
        chromosome_2 = random_selection(population, probabilities)

        # Create two new chromosomes from 2 chromosomes
        child = crossover(chromosome_1, chromosome_2)

        # Mutation
        if random.random() < mutation_probability:
            child = mutation(child)

        new_population.append(child)
        if fitness(child, maxFitness) == maxFitness:
            break
    return new_population

# Display the given chromosome
def display_chromosome(chrom, maxFitness):
    print(
        "Chromosome = {}".format(str(chrom), fitness(chrom, maxFitness))
    )

# Display the board of the given chromosome
def display_board(chrom):
    board = []

    for x in range(len(chrom)):
        board.append(["x"] * len(chrom))

    for i in range(len(chrom)):
        board[chrom[i]][i] = "Q"

    for line in board:
        print(" ".join(line))

if __name__ == "__main__":
    POPULATION_SIZE = 500

    while True:
        # say N = 8
        nq = int(input("Please enter the desired number of queens (0 to quit): "))
        if nq == 0:
            break

        maxFitness = (nq * (nq - 1)) / 2  # 8*7/2 = 28
        population = [random_chromosome(nq) for _ in range(POPULATION_SIZE)]

        generation = 1
        while (
            not maxFitness in [fitness(chrom, maxFitness) for chrom in population]
            and generation < 200
        ):

            population = genetic_algorithm(population, maxFitness)
            if generation % 10 == 0:
                print("=== Generation {} ===".format(generation))

            generation += 1

        fitness_of_chromosomes = [fitness(chrom, maxFitness) for chrom in population]

        best_chromosomes = population[
            fitness_of_chromosomes.index(max(fitness_of_chromosomes))
        ]

        if maxFitness in fitness_of_chromosomes:
            print("\nSolved in generation {}!".format(generation - 1))

            display_chromosome(best_chromosomes, maxFitness)

            display_board(best_chromosomes)

        else:
            print(
                "\nUnfortunately, we did not find the answer by generation {}. The best answer the algorithm found was:".format(
                    generation - 1
                )
            )
            display_board(best_chromosomes)
