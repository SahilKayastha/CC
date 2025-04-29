# Python program to solve N Queen Problem using backtracking

def print_solution(board):
    for row in board:
        print(' '.join('1' if cell else '0' for cell in row))

def is_safe(board, row, col, N):
    return not any(board[row][i] for i in range(col)) and \
           not any(board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))) and \
           not any(board[i][j] for i, j in zip(range(row, N), range(col, -1, -1)))

def solve_nq_util(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nq_util(board, col + 1, N):
                return True
            board[i][col] = 0
    return False

def solve_nq():
    N = int(input("Enter board size (N): "))
    board = [[0]*N for _ in range(N)]
    
    if solve_nq_util(board, 0, N):
        print(f"\nSolution for {N}-Queens problem:")
        print_solution(board)
    else:
        print("No solution exists")

solve_nq()
