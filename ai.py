import math
import random
from board import ROWS, COLS, make_move, check_winner, valid_locations, is_terminal

def score_window(window, piece):
    score = 0
    opp_piece = 'X' if piece == 'O' else 'O'
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(' ') == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(' ') == 2:
        score += 2
    if window.count(opp_piece) == 3 and window.count(' ') == 1:
        score -= 4
    return score

def evaluate_board(board, piece):
    score = 0
    
    center_array = [board[r][COLS//2] for r in range(ROWS)]
    score += center_array.count(piece) * 3

 
    for r in range(ROWS):
        for c in range(COLS - 3):
            score += score_window(board[r][c:c+4], piece)
    for c in range(COLS):
        col_array = [board[r][c] for r in range(ROWS)]
        for r in range(ROWS - 3):
            score += score_window(col_array[r:r+4], piece)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            score += score_window([board[r+i][c+i] for i in range(4)], piece)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            score += score_window([board[r-i][c+i] for i in range(4)], piece)
    return score

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_cols = valid_locations(board)
    terminal = is_terminal(board)
    if depth == 0 or terminal:
        if terminal:
            if check_winner(board, 'O'):
                return (None, 1000000)
            elif check_winner(board, 'X'):
                return (None, -1000000)
            else:
                return (None, 0)
        else:
            return (None, evaluate_board(board, 'O'))

    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_cols)
        for col in valid_cols:
            temp_board = [row.copy() for row in board]
            make_move(temp_board, col, 'O')
            new_score = minimax(temp_board, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value, best_col = new_score, col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_cols)
        for col in valid_cols:
            temp_board = [row.copy() for row in board]
            make_move(temp_board, col, 'X')
            new_score = minimax(temp_board, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value, best_col = new_score, col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value
