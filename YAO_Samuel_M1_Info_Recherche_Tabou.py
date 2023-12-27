import random

def initialiser_solution():
    return random.sample(range(8), 8)

def generer_configurations_voisines(configuration_initiale):
    configurations_voisines = []

    for _ in range(5):
        # On choisit aléatoirement une reine à déplacer
        reine_a_deplacer = random.randint(0, 7)

        # On génère une configuration voisine en déplaçant la reine choisie
        nouvelle_configuration = configuration_initiale.copy()
        nouvelle_configuration[reine_a_deplacer] = random.randint(0, 7)

        # On ajoute la nouvelle configuration à la liste des voisins
        configurations_voisines.append(nouvelle_configuration)

    return configurations_voisines

def conflit(solution):
    menaces = 0
    taille = len(solution)
    for i in range(taille):
        for j in range(i + 1, taille):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                menaces += 1
    return menaces

def recherche_tabou():
    Tabou = []
    NT = []
    init = initialiser_solution()
    s_best = init
    s_prime = s_best
    k = 0
    taille_liste_tabou = 50

    Tabou.append(s_best)

    while True:
        voisins = generer_configurations_voisines(s_prime)
        min_conflits = float('inf')
        meilleur_voisin = None

        for voisin in voisins:
            if voisin not in Tabou:
                conf_voisin = conflit(voisin)
                if conf_voisin < min_conflits:
                    min_conflits = conf_voisin
                    meilleur_voisin = voisin

        if meilleur_voisin is not None:
            s_prime = meilleur_voisin

        if conflit(s_prime) < conflit(s_best):
            s_best = s_prime

        print(f'***Meilleure solution : {s_best} avec {conflit(s_best)} conflits à l\'itération {k + 1}***')
        print(f'La liste Tabou étant {Tabou}')

        Tabou.append(s_prime)
        if len(Tabou) > taille_liste_tabou:
            Tabou.pop(0)

        if conflit(s_best) == 0:
            print(f'Solution optimale trouvée : {s_best} avec 0 conflit à l\'itération {k + 1}.')
            break

        k += 1

recherche_tabou()
