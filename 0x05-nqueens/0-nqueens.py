#!/usr/bin/python3
import sys

def print_solution(board):
    """Print the solution in the required format"""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_util(board, col):
    """Use backtracking to find all solutions"""
    if col >= len(board):
        print_solution(board)
        return True
    
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0  # backtrack
    return res

def solve_nqueens(N):
    """Initialize the board and solve the N-Queens problem"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens_util(board, 0):
        print("No solution")

if __name__ == "__main__":
    # Validate the input arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

