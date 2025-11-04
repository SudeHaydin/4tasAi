import tkinter as tk
from gui import ConnectFourGUI

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFourGUI(root)
    root.mainloop()
