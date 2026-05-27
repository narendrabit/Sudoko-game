# 🧩 Sudoku Helper & Interactive Game

An interactive, terminal-based Sudoku game and smart helper engine written in Python. It features custom puzzles of varying difficulties, real-time board rendering, dynamic move validation, and a mathematically intelligent hint generator powered by an "Automatic Naked Single" algorithm.

---

## ✨ Features

- 🎮 **Interactive Gameplay**: Play classic 9x9 Sudoku directly from your command-line interface with intuitive coordinates (1-9 row/col indexing).
- 🧩 **Multi-Difficulty Database**: Built-in puzzles categorized into **Easy**, **Medium**, and **Hard** difficulties, loaded randomly to ensure high replayability.
- 🤖 **Intelligent Hint Engine ("Naked Single" Solver)**: Analyzes the current state of the board to find cells where only *one* number is mathematically possible according to standard Sudoku rules, providing instant strategic guidance.
- 🧮 **Real-Time Rule Validation**: Dynamically validates column, row, and 3x3 subgrid constraints for every move to prevent illegal entries.
- 📊 **Elegant Board Display**: Features a structured, ASCII-based 9x9 grid layout with clean section dividers for sub-grids, displaying empty spots as dots (`.`).
- 🏆 **Automatic Win Detection**: Monitors the board's state and announces a victory celebration immediately when all cells are correctly filled.

---

## 🚀 Getting Started

### Prerequisites

You need **Python 3.x** installed on your machine. To verify, run:

```bash
python --version

Installation
Clone the repository and navigate into the project directory:

bash
git clone https://github.com/narendrabit/sudoku-helper.git
cd sudoku-helper
Running the Game
Simply run the script using Python:

bash
python sudoko.py


🖥️ How to Play
Launch the Game: Enter your preferred difficulty (easy, medium, or hard).
Options Menu:
1: Enter a Number: Provide a target Row (1-9), Column (1-9), and the Number (1-9) you want to place.
2: Get a SMART Hint: The AI will scan the entire grid and recommend a guaranteed legal number placement.
3: Exit: Close the application.
Solve the Puzzle: Complete the board correctly to win!  


📐 Project Architecture
The code follows a clean, modular structure divided into logic sections:

Module / Function	Description
puzzles_db	Hierarchical database containing pre-defined board layouts for all difficulties.
get_random_board()	Selects and deeply clones a board configuration using the copy module.
print_board()	Renders the beautiful ASCII representation of the Sudoku grid in the terminal.
is_valid()	Validation logic implementing traditional Sudoku rules (checks row, column, and 3x3 block).
get_smart_hint()	Evaluates cell constraints and identifies Naked Singles (cells with exactly one valid digit option).
main()	Orchestrates the primary game loop, options menu, try-except input handling, and victory verification.


🧾 Sample Interface Preview

--- WELCOME TO SUDOKU HELPER ---
Select Difficulty (easy, medium, hard): easy

 Current Sudoku Board:
 -----------------------
 | 5 3 . | . 7 . | . . . | 
 | 6 . . | 1 9 5 | . . . | 
 | . 9 8 | . . . | . 6 . | 
 -----------------------
 | 8 . . | . 6 . | . . 3 | 
 | 4 . . | 8 . 3 | . . 1 | 
 | 7 . . | . 2 . | . . 6 | 
 -----------------------
 | . 6 . | . . . | 2 8 . | 
 | . . . | 4 1 9 | . . 5 | 
 | . . . | . 8 . | . 7 9 | 
 -----------------------

Options:
1. Enter a number
2. Get a SMART Hint (Helper)
3. Exit
Choose option (1/2/3): 2
🤖 Analyzing board...
💡 HINT: At Row 1, Col 3, the ONLY possible number is 1!

🤝 Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create.

Fork the Project.
Create your Feature Branch (git checkout -b feature/AmazingFeature).
Commit your Changes (git commit -m 'Add some AmazingFeature').
Push to the Branch (git push origin feature/AmazingFeature).
Open a Pull Request.
