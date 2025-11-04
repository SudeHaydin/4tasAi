import math
import random
import time

from board import ROWS, COLS, create_board, make_move, check_winner, valid_locations, is_terminal
from ai import minimax, evaluate_board 



def random_agent_move(board):
    
    valid_cols = valid_locations(board)
    if valid_cols:
        return random.choice(valid_cols)
    return None


def run_simulation(depth_o, total_games):
    """
    Minimax AI'ı (O) Rastgele Ajana (X) karşı belirli sayıda oynatır.
    """
    wins_o = 0 
    wins_x = 0 
    draws = 0  
    print(f"\n--- AI ({depth_o} Derinlik) vs. Rastgele Ajan Testi ---")
    print(f"Toplam Oyun Sayısı: {total_games}\n")

    for game_num in range(1, total_games + 1):
        board = create_board()
        turn = random.randint(0, 1) 
        
    
        game_over = False
        
        start_time = time.time()
        
        while not game_over:
            
          
            if turn == 0:
                
                col, score = minimax(board, depth_o, -math.inf, math.inf, True)
                piece = 'O'
            
            
            else:
                
                col = random_agent_move(board)
                piece = 'X'
                
            
            
            if col is not None and make_move(board, col, piece):
                
               
                if check_winner(board, piece):
                    if piece == 'O':
                        wins_o += 1
                        print(f"Oyun {game_num}: AI (O) Kazandı! ({time.time() - start_time:.2f} sn)")
                    else:
                        wins_x += 1
                        print(f"Oyun {game_num}: Rastgele Ajan (X) Kazandı! ({time.time() - start_time:.2f} sn)")
                    game_over = True 
                
               
                elif len(valid_locations(board)) == 0:
                    draws += 1
                    print(f"Oyun {game_num}: Berabere! ({time.time() - start_time:.2f} sn)")
                    game_over = True 
                
                turn = 1 - turn 
            
            elif col is None:
                
                game_over = True
                break
        
  
    print("\n" + "="*40)
    print("        NİHAİ TEST SONUÇLARI")
    print("="*40)
    print(f"Toplam Oyun: {total_games}")
    print(f"AI (O) Galibiyeti: {wins_o} (% {wins_o / total_games * 100:.2f})")
    print(f"Rastgele Ajan (X) Galibiyeti: {wins_x} (% {wins_x / total_games * 100:.2f})")
    print(f"Berabere: {draws} (% {draws / total_games * 100:.2f})")
    print("="*40)
    
    return wins_o, total_games



if __name__ == "__main__":
    
  
    MINIMAX_DEPTH = 4  
    
    NUMBER_OF_GAMES = 20
    
    run_simulation(MINIMAX_DEPTH, NUMBER_OF_GAMES)