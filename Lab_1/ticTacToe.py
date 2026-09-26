def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] \
                and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] \
            and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] \
            and board[0][2] != " ":
        return board[0][2]
    if all(cell != " " for row in board for cell in row):
        return "DRAW"
    return None

def minimax(board, depth, maximizing):
    result = check_winner(board)
    if result == "O":
        return 10 - depth
    if result == "X":
        return depth - 10
    if result == "DRAW":
        return 0
    if maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = float("-inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


# Main game
board = [[" " for _ in range(3)] for _ in range(3)]
print("Human : X")
print("Bot : O")
while True:
    display_board(board)
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if board[row][col] != " ":
        print("Invalid move!")
        continue
    board[row][col] = "X"
    result = check_winner(board)
    if result:
        display_board(board)
        print("Result:", result)
        break
    ai_row, ai_col = best_move(board)
    board[ai_row][ai_col] = "O"
    result = check_winner(board)
    if result:
        display_board(board)
        print("Result:", result)
        break

