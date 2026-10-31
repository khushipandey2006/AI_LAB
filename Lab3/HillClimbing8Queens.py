import random

def print_board(board):
    for r in range(8):
        row_str = ""
        for c in range(8):
            if board[c] == r:
                row_str += "Q "
            else:
                row_str += ". "
        print(row_str)
    print()

def calculate_cost(board):
    cost = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1
    return cost

def get_neighbors(board):
    neighbors = []
    for col in range(8):
        for row in range(8):
            if board[col] != row:
                neighbor = list(board)
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climbing():
    current_board = [random.randint(0, 7) for _ in range(8)]
    print("Initial State:")
    print_board(current_board)
    current_cost = calculate_cost(current_board)
    print(f"Initial Cost (Attacking pairs): {current_cost}\n")
    step = 0
    while True:
        step += 1
        neighbors = get_neighbors(current_board)
        best_neighbor = current_board
        best_cost = current_cost
        for neighbor in neighbors:
            cost = calculate_cost(neighbor)
            if cost < best_cost:
                best_cost = cost
                best_neighbor = neighbor
        if best_cost >= current_cost:
            break
        current_board = best_neighbor
        current_cost = best_cost
        
        if current_cost == 0:
            break
    print(f"Final State (Step {step}):")
    print_board(current_board)
    print(f"Final Cost: {current_cost}")
    if current_cost == 0:
        print("Solution found!")
    else:
        print("Stuck in local minimum!")
if __name__ == "__main__":
    hill_climbing()