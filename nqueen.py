def main():
    n = int(input("Enter the number of queens: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)

    if solutions:
        print(f"\nTotal solutions found: {len(solutions)}\n")
        print(solutions)
        for index, sol in enumerate(solutions, start=1):
            print(f"Solution {index}:")
            for row in sol:
                print(" ".join(str(x) for x in row))
            print()
    else:
        print("No solution exists.")

def solve_n_queens(board, col, n, solutions):
    if col == n:
        # Found a solution; store a deep copy of the board
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens(board, col + 1, n, solutions)
            board[i][col] = 0 

def is_safe(board, row, col, n):
    # Check row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

if __name__ == "__main__":
    main()
