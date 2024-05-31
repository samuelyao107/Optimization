import random

def initialize_solution():
    return random.sample(range(8), 8)

def generate_neighboring_configurations(initial_configuration):
    neighboring_configurations = []

    for _ in range(5):
        # Randomly choose a queen to move
        queen_to_move = random.randint(0, 7)

        # Generate a neighboring configuration by moving the chosen queen
        new_configuration = initial_configuration.copy()
        new_configuration[queen_to_move] = random.randint(0, 7)

        # Add the new configuration to the list of neighbors
        neighboring_configurations.append(new_configuration)

    return neighboring_configurations

def conflict(solution):
    threats = 0
    size = len(solution)
    for i in range(size):
        for j in range(i + 1, size):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                threats += 1
    return threats

def tabu_search():
    Tabu = []
    init = initialize_solution()
    s_best = init
    s_prime = s_best
    k = 0
    tabu_list_size = 50

    Tabu.append(s_best)

    while True:
        neighbors = generate_neighboring_configurations(s_prime)
        min_conflicts = float('inf')
        best_neighbor = None

        for neighbor in neighbors:
            if neighbor not in Tabu:
                neighbor_conflicts = conflict(neighbor)
                if neighbor_conflicts < min_conflicts:
                    min_conflicts = neighbor_conflicts
                    best_neighbor = neighbor

        if best_neighbor is not None:
            s_prime = best_neighbor

        if conflict(s_prime) < conflict(s_best):
            s_best = s_prime

        print(f'***Best solution: {s_best} with {conflict(s_best)} conflicts at iteration {k + 1}***')
        print(f'Tabu list is {Tabu}')

        Tabu.append(s_prime)
        if len(Tabu) > tabu_list_size:
            Tabu.pop(0)

        if conflict(s_best) == 0:
            print(f'Optimal solution found: {s_best} with 0 conflicts at iteration {k + 1}.')
            break

        k += 1

tabu_search()
