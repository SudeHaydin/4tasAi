ROWS = 6
COLS = 7

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def make_move(board, col, piece):
    for r in reversed(range(ROWS)):
        if board[r][col] == ' ':
            board[r][col] = piece
            return True
    return False

def check_winner(board, piece):
    
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False

def valid_locations(board):
    return [c for c in range(COLS) if board[0][c] == ' ']

def is_terminal(board):
    return check_winner(board, 'X') or check_winner(board, 'O') or len(valid_locations(board)) == 0
