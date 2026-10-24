from collections import deque

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    moves = [-3, 3, -1, 1]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for move in moves:
            new_pos = zero + move

            if new_pos < 0 or new_pos >= 9:
                continue

            if move == -3 and row == 0:
                continue
            if move == 3 and row == 2:
                continue
            if move == -1 and col == 0:
                continue
            if move == 1 and col == 2:
                continue

            new_state = list(state)
            new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None


start = tuple(map(int, input("Enter initial state: ").split()))
goal = tuple(map(int, input("Enter goal state: ").split()))

result = bfs(start, goal)

if result:
    print("Solution found:")
    for state in result:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
    print("Total moves:", len(result) - 1)
else:
    print("No solution found")