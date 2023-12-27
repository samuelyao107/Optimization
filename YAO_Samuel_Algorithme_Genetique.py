import random

# Création de chromosomes aléatoires
def chromosome_aleatoire(taille):
    return [random.randint(0, taille - 1) for _ in range(taille)]

# Calcul du fitness
def fitness(chromosome, maxFitness):
    collisions_horizontales = (
        sum([chromosome.count(reine) - 1 for reine in chromosome]) / 2
    )
    collisions_diagonales = 0

    n = len(chromosome)
    diagonale_gauche = [0] * (2 * n - 1)
    diagonale_droite = [0] * (2 * n - 1)
    for i in range(n):
        diagonale_gauche[i + chromosome[i] - 1] += 1
        diagonale_droite[len(chromosome) - i + chromosome[i] - 2] += 1

    for i in range(2 * n - 1):
        contre = 0
        if diagonale_gauche[i] > 1:
            contre += diagonale_gauche[i] - 1
        if diagonale_droite[i] > 1:
            contre += diagonale_droite[i] - 1
        collisions_diagonales += contre

    # 28 - (2 + 3) = 23
    return int(maxFitness - (collisions_horizontales + collisions_diagonales))

# Croisement entre deux chromosomes
def croisement(x, y):
    n = len(x)
    enfant = [0] * n
    for i in range(n):
        c = random.randint(0, 1)
        if c < 0.5:
            enfant[i] = x[i]
        else:
            enfant[i] = y[i]
    return enfant

# Mutation en changeant la valeur d'un indice aléatoire du chromosome
def mutation(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(0, n - 1)
    x[c] = m
    return x

# Calcul de la probabilité
def probabilite(chromosome, maxFitness):
    return fitness(chromosome, maxFitness) / maxFitness

# Sélection par roulette
def choix_aleatoire(population, probabilites):
    population_avec_probabilite = zip(population, probabilites)
    total = sum(w for c, w in population_avec_probabilite)
    r = random.uniform(0, total)
    jusqu_a = 0
    for c, w in zip(population, probabilites):
        if jusqu_a + w >= r:
            return c
        jusqu_a += w
    assert False, "On ne devrait pas arriver ici"

# Algorithme génétique
def algorithme_genetique(population, maxFitness):
    probabilite_mutation = 0.1
    nouvelle_population = []
    population_triee = []
    probabilites = []
    for n in population:
        f = fitness(n, maxFitness)
        probabilites.append(f / maxFitness)
        population_triee.append([f, n])

    population_triee.sort(reverse=True)

    # Élitisme
    nouvelle_population.append(population_triee[0][1])  # le meilleur génome
    nouvelle_population.append(population_triee[-1][1])  # le pire génome

    for i in range(len(population) - 2):
        chromosome_1 = choix_aleatoire(population, probabilites)
        chromosome_2 = choix_aleatoire(population, probabilites)

        # Création de deux nouveaux chromosomes à partir de 2 chromosomes
        enfant = croisement(chromosome_1, chromosome_2)

        # Mutation
        if random.random() < probabilite_mutation:
            enfant = mutation(enfant)

        nouvelle_population.append(enfant)
        if fitness(enfant, maxFitness) == maxFitness:
            break
    return nouvelle_population

# Affiche le chromosome donné
def afficher_chromosome(chrom, maxFitness):
    print(
        "Chromosome = {}".format(str(chrom), fitness(chrom, maxFitness))
    )

# Affiche le plateau du chromosome donné
def afficher_plateau(chrom):
    tableau = []

    for x in range(len(chrom)):
        tableau.append(["x"] * len(chrom))

    for i in range(len(chrom)):
        tableau[chrom[i]][i] = "Q"

    for ligne in tableau:
        print(" ".join(ligne))

if __name__ == "__main__":
    TAILLE_POPULATION = 500

    while True:
        # disons N = 8
        nq = int(input("Veuillez entrer le nombre de reines souhaité (0 pour quitter): "))
        if nq == 0:
            break

        maxFitness = (nq * (nq - 1)) / 2  # 8*7/2 = 28
        population = [chromosome_aleatoire(nq) for _ in range(TAILLE_POPULATION)]

        generation = 1
        while (
            not maxFitness in [fitness(chrom, maxFitness) for chrom in population]
            and generation < 200
        ):

            population = algorithme_genetique(population, maxFitness)
            if generation % 10 == 0:
                print("=== Génération {} ===".format(generation))

            generation += 1

        fitness_des_chromosomes = [fitness(chrom, maxFitness) for chrom in population]

        meilleurs_chromosomes = population[
            fitness_des_chromosomes.index(max(fitness_des_chromosomes))
        ]

        if maxFitness in fitness_des_chromosomes:
            print("\nRésolu dans la génération {} !".format(generation - 1))

            afficher_chromosome(meilleurs_chromosomes, maxFitness)

            afficher_plateau(meilleurs_chromosomes)

        else:
            print(
                "\nMalheureusement, nous n'avons pas trouvé la réponse jusqu'à la génération {}. La meilleure réponse que l'algorithme a trouvée était :".format(
                    generation - 1
                )
            )
            afficher_plateau(meilleurs_chromosomes)
