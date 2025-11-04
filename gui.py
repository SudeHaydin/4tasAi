import tkinter as tk
from tkinter import messagebox
import math
from board import create_board, make_move, check_winner
from ai import minimax, valid_locations

CELL_SIZE = 80
ROWS = 6
COLS = 7

class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")
        self.board = create_board()
        self.turn = 0 
        self.create_widgets()

    def create_widgets(self):
       
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        self.buttons = []
        for c in range(COLS):
            btn = tk.Button(top_frame, text=str(c + 1), font=("Arial", 14, "bold"),
                            width=6, bg="#A0522D", fg="white",
                            command=lambda col=c: self.player_move(col))
            btn.grid(row=0, column=c, padx=2)
            self.buttons.append(btn)

        
        self.canvas = tk.Canvas(self.root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="#004080")
        self.canvas.pack(padx=10, pady=10)

        self.draw_board()

    def draw_board(self):
        """Tüm tahtayı çiz."""
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x1 = c * CELL_SIZE + 5
                y1 = r * CELL_SIZE + 5
                x2 = x1 + CELL_SIZE - 10
                y2 = y1 + CELL_SIZE - 10
                piece = self.board[r][c]

                if piece == 'X':
                    color = "pink"
                elif piece == 'O':
                    color = "orange"
                else:
                    color = "white"

                self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black", width=2)

    def player_move(self, col):
        """Oyuncunun hamlesi."""
        if self.turn != 0 or self.board[0][col] != ' ':
            return

        make_move(self.board, col, 'X')
        self.draw_board()

        if check_winner(self.board, 'X'):
            self.show_winner("Tebrikler! Oyuncu kazandı!")
            return

        if len(valid_locations(self.board)) == 0:
            self.show_winner("Berabere!")
            return

        self.turn = 1
        self.root.after(500, self.ai_move)

    def ai_move(self):
        """Yapay zekâ hamlesi."""
        col, _ = minimax(self.board, 4, -math.inf, math.inf, True)
        make_move(self.board, col, 'O')
        self.draw_board()

        if check_winner(self.board, 'O'):
            self.show_winner(" AI kazandı!")
            return

        if len(valid_locations(self.board)) == 0:
            self.show_winner("Berabere!")
            return

        self.turn = 0

    def show_winner(self, message):
        """Kazananı gösterip oyunu bitir."""
        self.draw_board()
        messagebox.showinfo("Oyun Bitti", message)
        self.root.destroy()
