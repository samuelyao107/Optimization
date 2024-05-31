import random
import math
import sys

# The initial temperature is set here to 50 and the cooling rate to 0.95
# Initialize the starting position randomly
def initialize_solution():
    return [random.randint(1, 8) for _ in range(8)]

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

# Function to determine conflicts
def conflict(solution):
    threats = 0
    size = len(solution)
    for i in range(size):
        for j in range(i + 1, size):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                threats += 2
    return threats

# Function to calculate the probability
def probability(s, s_prime, T):
    return math.exp((conflict(s) - conflict(s_prime)) / T)

init = initialize_solution()

# Initial temperature
T = 50

k = 0
# Limit the number of recursions to 1500 to avoid unpredictable program behavior
sys.setrecursionlimit(800)
while True:
    print(f"The initial configuration is {init} with {conflict(init)} conflicts")
    initial_conflicts = conflict(init)
    initial_neighbors = generate_neighboring_configurations(init)

    # Randomly choose an element
    x = random.randrange(0, len(initial_neighbors))
    elem = initial_neighbors[x]
    conflicts = conflict(elem)
    r = random.uniform(0, 1)
    if r < probability(init, elem, T):
        init = elem.copy()
        print(f"The solution chosen at iteration {k} is {init} with {conflict(init)} conflicts")
        print(f"The temperature is {T}")
        min_conflicts = conflicts
        T = 0.95 * T
    if min_conflicts == 0:
        print(f"The final solution obtained at iteration {k} is {elem}, with a temperature of {T}")
        break

    k += 1
