import random

#initialisation de la position de départ de facon aléatoire
def initialiser_solution():
    return [random.randint(1, 8) for _ in range(8)]

# Détermination des cinq voisins
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
                menaces += 1
    return menaces


def main():
    #initialisation
    init = initialiser_solution()
    print("La configuration initiale est ",init)
    print("Le nombre de conflits de la configuration initiale est: ", conflit(init))
    voisins = generer_configurations_voisines(init)
    print(voisins)
    conflits_init = conflit(init)
    min = conflits_init
    min1=0
    minsol=[]
    #Le nombre d'itération maximal est fixé à 1000
    for j in range (1000):

     for element in voisins:
        print(f"Le nombre de conflits de {element} est {conflit(element)}")
        if conflit(element)<min:
            min=conflit(element)
            minsol=element

     if min ==0 :
        return f"La solution trouvée est :{element} de nombre de conflits: {min}"
        break
     elif min1 == min:
         break
     else:
         if minsol != []:
             print(f"La solution minimisant le conflit est {minsol} de nombres de conflits : {min}")

         else:
             print(f"La solution minimisant le conflit a comme nombre de conflits : {min}")
         voisins = generer_configurations_voisines(minsol)
         min1=conflit(minsol)
    if min !=0  :
        print(f"Aucune solution trouvée mais la configuration minimisant les conflits est {minsol} de conflits: {min}")


main()