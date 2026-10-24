import random
import math

def simulated_annealing(graph, heuristic, start, goal):
    current = start
    best = start

    temperature = 100
    cooling_rate = 0.95
    min_temperature = 0.01

    while temperature > min_temperature:

        if current == goal:
            return current

        neighbors = graph[current]

        if not neighbors:
            break

        next_node = random.choice(neighbors)

        delta = heuristic[next_node] - heuristic[current]

        if delta < 0:
            current = next_node

        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                current = next_node

        if heuristic[current] < heuristic[best]:
            best = current

        temperature *= cooling_rate

    return best


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors separated by space: ").split()
    graph[node] = neighbors

heuristic = {}

for node in graph:
    heuristic[node] = int(input("Enter heuristic for " + node + ": "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

result = simulated_annealing(graph, heuristic, start, goal)

if result == goal:
    print("Goal found:", result)
else:
    print("Best state found:", result)
