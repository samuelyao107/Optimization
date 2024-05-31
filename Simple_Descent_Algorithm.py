import random

# Initialize the starting position randomly
def initialize_solution():
    return [random.randint(1, 8) for _ in range(8)]

# Determining five neighbors
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
                threats += 1
    return threats

def main():
    # Initialization
    init = initialize_solution()
    print("The initial configuration is ", init)
    print("The number of conflicts in the initial configuration is: ", conflict(init))
    neighbors = generate_neighboring_configurations(init)
    print(neighbors)
    initial_conflicts = conflict(init)
    min_conflicts = initial_conflicts
    min_conflicts_prev = 0
    min_sol = []
    # The maximum number of iterations is set to 1000
    for j in range(1000):
        for element in neighbors:
            print(f"The number of conflicts in {element} is {conflict(element)}")
            if conflict(element) < min_conflicts:
                min_conflicts = conflict(element)
                min_sol = element

        if min_conflicts == 0:
            return f"The solution found is: {element} with number of conflicts: {min_conflicts}"
            break
        elif min_conflicts_prev == min_conflicts:
            break
        else:
            if min_sol:
                print(f"The solution minimizing the conflict is {min_sol} with number of conflicts: {min_conflicts}")
            else:
                print(f"The solution minimizing the conflict has number of conflicts: {min_conflicts}")
            neighbors = generate_neighboring_configurations(min_sol)
            min_conflicts_prev = conflict(min_sol)

    if min_conflicts != 0:
        print(f"No solution found, but the configuration minimizing conflicts is {min_sol} with conflicts: {min_conflicts}")

main()
