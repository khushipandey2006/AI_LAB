def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], start)]

    g_cost = {start: 0}
    parent = {}

    while open_list:
        open_list.sort()

        f, current = open_list.pop(0)

        if current == goal:
            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path, g_cost[goal]

        for neighbor, cost in graph[current].items():
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = current

                f_cost = new_cost + heuristic[neighbor]

                open_list = [item for item in open_list if item[1] != neighbor]
                open_list.append((f_cost, neighbor))

    return None, None


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    graph[node] = {}

    edges = int(input("Enter number of neighbors: "))

    for j in range(edges):
        neighbor, cost = input("Enter neighbor and cost: ").split()
        graph[node][neighbor] = int(cost)

heuristic = {}

for node in graph:
    heuristic[node] = int(input("Enter heuristic for " + node + ": "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path, cost = astar(graph, heuristic, start, goal)

if path:
    print("Optimal path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found")