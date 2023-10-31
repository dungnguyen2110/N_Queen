def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]

    def print_solution(board):
        for row in board:
            print(" ".join("Q" if cell == 1 else "." for cell in row))
        print("\n")

    def bfs():
        queue = [(0, board)]
        while queue:
            row, current_board = queue.pop(0)
            if row == N:
                # Found a solution
                print_solution(current_board)
            for col in range(N):
                if is_safe(current_board, row, col):
                    new_board = [row[:] for row in current_board]
                    new_board[row][col] = 1
                    queue.append((row + 1, new_board))

    bfs()

N = int(input("input N for N-queens "))
solve_n_queens(N)