import random
import math
import sys



# La Température initiale est fixée ici à 50 et le taux de refroidissement à 0.95
#initialisation de la position de départ de facon aléatoire
def initialiser_solution():
    return [random.randint(1, 8) for _ in range(8)]

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

#Fonction de détermination des conflits
def conflit(solution):
    menaces = 0
    taille = len(solution)
    for i in range(taille):
        for j in range(i + 1, taille):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                menaces += 2
    return menaces


#Fonction de calcul de la probabilité

def probabilite(s,s_prim,T):
    return math.exp((conflit(s)-conflit(s_prim))/T)
init=initialiser_solution()


#Température initiale
T=50


k=0
#On limite le nombre de récursion à 1500 pour éviter les comportements imprévisibles du programme
sys.setrecursionlimit(800)
while True:

    print(f"La configuration initiale est {init} de conflit {conflit(init)}")
    conflits_init= conflit(init)
    voisins_init=generer_configurations_voisines(init)

    #Choix de l'élément de facon aléatoire
    x = random.randrange(0, len(voisins_init))
    elem=voisins_init[x]
    conflits=conflit(elem)
    r = random.uniform(0, 1)
    if r <probabilite(init,elem,T):
            init=elem.copy()
            print(f"La solution choisie à la {k}-ième itérration est {init} de conflit {conflit(init)}")
            print(f"La température est {T}")
            min=conflits
            T = 0.95 * T
    if min==0:
        print(f"La solution finale obtenue à la {k}-ième itérration est {elem}, la température étant de {T}")
        break


    k+=1


