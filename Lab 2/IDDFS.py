def dls(graph, node, goal, depth, path):
    if node == goal:
        return path

    if depth == 0:
        return None

    for neighbor in graph[node]:
        if neighbor not in path:
            result = dls(graph, neighbor, goal, depth - 1, path + [neighbor])

            if result:
                return result

    return None


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print("Depth limit:", depth)

        result = dls(graph, start, goal, depth, [start])

        if result:
            return result

    return None


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors separated by space: ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

result = iddfs(graph, start, goal, max_depth)

if result:
    print("Goal found!")
    print("Path:", " -> ".join(result))
else:
    print("Goal not found")