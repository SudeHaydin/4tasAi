
This project was developed for **CENG 3511: Artificial Intelligence Midterm Project**.

The goal of this project is to design and implement an **AI agent** that can play the classic Connect Four game against a human player using the **Minimax algorithm with Alpha-Beta Pruning**.

- The game is played on a 6x7 grid.
- Two players take turns dropping their pieces ("X" for human, "O" for AI).
- The first to connect 4 in a row (horizontally, vertically, or diagonally) wins.

The AI uses:
- **Minimax Algorithm** for decision-making.
- **Alpha-Beta Pruning** to optimize performance.
- A **heuristic evaluation function** that scores board positions based on possible winning combinations.

The AI was tested through real gameplay interactions.
- Demonstrates **high strategic superiority**, validating the heuristic design.
- Shows **flawless tactical execution**, confirming efficient threat detection.


- Python 3
- Tkinter (for GUI)
- Custom game logic and AI scripts


1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ConnectFourAI.git
