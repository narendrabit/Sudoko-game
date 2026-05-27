import random

import copy



# ==========================================

# 1. SETUP & DATA (Member 1)

# ==========================================



puzzles_db = {

    "easy": [

        [

            [5, 3, 0, 0, 7, 0, 0, 0, 0],

            [6, 0, 0, 1, 9, 5, 0, 0, 0],

            [0, 9, 8, 0, 0, 0, 0, 6, 0],

            [8, 0, 0, 0, 6, 0, 0, 0, 3],

            [4, 0, 0, 8, 0, 3, 0, 0, 1],

            [7, 0, 0, 0, 2, 0, 0, 0, 6],

            [0, 6, 0, 0, 0, 0, 2, 8, 0],

            [0, 0, 0, 4, 1, 9, 0, 0, 5],

            [0, 0, 0, 0, 8, 0, 0, 7, 9]

        ]

    ],

    "medium": [

        [

            [0, 0, 0, 2, 6, 0, 7, 0, 1],

            [6, 8, 0, 0, 7, 0, 0, 9, 0],

            [1, 9, 0, 0, 0, 4, 5, 0, 0],

            [8, 2, 0, 1, 0, 0, 0, 4, 0],

            [0, 0, 4, 6, 0, 2, 9, 0, 0],

            [0, 5, 0, 0, 0, 3, 0, 2, 8],

            [0, 0, 9, 3, 0, 0, 0, 7, 4],

            [0, 4, 0, 0, 5, 0, 0, 3, 6],

            [7, 0, 3, 0, 1, 8, 0, 0, 0]

        ]

    ],

    "hard": [

        [

            [0, 2, 0, 6, 0, 8, 0, 0, 0],

            [5, 8, 0, 0, 0, 9, 7, 0, 0],

            [0, 0, 0, 0, 4, 0, 0, 0, 0],

            [3, 7, 0, 0, 0, 0, 5, 0, 0],

            [6, 0, 0, 0, 0, 0, 0, 0, 4],

            [0, 0, 8, 0, 0, 0, 0, 1, 3],

            [0, 0, 0, 0, 2, 0, 0, 0, 0],

            [0, 0, 9, 8, 0, 0, 0, 3, 6],

            [0, 0, 0, 3, 0, 6, 0, 9, 0]

        ]

    ]

}



def get_random_board(difficulty):

    if difficulty not in puzzles_db:

        difficulty = "easy" # Default to easy if input is wrong

    selected = random.choice(puzzles_db[difficulty])

    return copy.deepcopy(selected)



# ==========================================

# 2. BOARD DISPLAY (Member 2)

# (Used your friend's clean format here)

# ==========================================

def print_board(board):

    print("\n Current Sudoku Board:")

    print(" -----------------------")

    for i in range(9):

        print(" |", end=" ")

        for j in range(9):

            if board[i][j] == 0:

                print(".", end=" ")

            else:

                print(board[i][j], end=" ")

            if (j + 1) % 3 == 0: # Add vertical separator

                print("|", end=" ")

        print()

        if (i + 1) % 3 == 0: # Add horizontal separator

            print(" -----------------------")



# ==========================================

# 3. VALIDATION LOGIC (Member 3)

# (Your friend's logic was perfect, kept it)

# ==========================================

def is_valid(board, row, col, num):

    # Check row

    if num in board[row]:

        return False



    # Check column

    for i in range(9):

        if board[i][col] == num:

            return False



    # Check 3x3 box

    start_row = (row // 3) * 3

    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):

        for j in range(start_col, start_col + 3):

            if board[i][j] == num:

                return False



    return True



# ==========================================

# 4. HELPER INTELLIGENCE (Member 4)

# (UPGRADED: From "Manual" to "Automatic Naked Single")

# ==========================================

def get_smart_hint(board):

    """

    Scans the WHOLE board to find a cell where only ONE number is possible.

    """

    for row in range(9):

        for col in range(9):

            if board[row][col] == 0:

                possible_nums = []

                for num in range(1, 10):

                    if is_valid(board, row, col, num):

                        possible_nums.append(num)

                

                # FOUND IT! Only one number fits here.

                if len(possible_nums) == 1:

                    return row, col, possible_nums[0]

    

    return None



# ==========================================

# 5. MAIN PROGRAM (Member 5)

# ==========================================

def main():

    print("\n--- WELCOME TO SUDOKU HELPER ---")

    

    # 1. Ask Difficulty

    diff = input("Select Difficulty (easy, medium, hard): ").lower().strip()

    board = get_random_board(diff)



    while True:

        print_board(board)

        

        print("\nOptions:")

        print("1. Enter a number")

        print("2. Get a SMART Hint (Helper)")

        print("3. Exit")

        

        choice = input("Choose option (1/2/3): ")

        

        if choice == "1":

            try:

                # Using friend's logic but added -1 for index correction

                r = int(input("Row (1-9): ")) - 1

                c = int(input("Col (1-9): ")) - 1

                n = int(input("Number (1-9): "))

                

                if 0 <= r < 9 and 0 <= c < 9:

                    if board[r][c] != 0:

                        print("❌ Cell is already full!")

                    elif is_valid(board, r, c, n):

                        board[r][c] = n

                        print("✅ Number placed successfully!")

                    else:

                        print("❌ Invalid move! Rule violation.")

                else:

                    print("❌ Out of bounds.")

            except ValueError:

                print("❌ Please enter valid numbers.")

        

        elif choice == "2":

            # This is the INTELLIGENT part

            print("🤖 Analyzing board...")

            hint = get_smart_hint(board)

            

            if hint:

                r, c, val = hint

                print(f"💡 HINT: At Row {r+1}, Col {c+1}, the ONLY possible number is {val}!")

            else:

                print("⚠️ No simple hints found. You might need to guess!")

        

        elif choice == "3":

            print("Thank you for using Sudoku Helper!")

            break

            

        else:

            print("Invalid choice!")



        # Win Check

        if all(0 not in row for row in board):

            print_board(board)

            print("🎉 CONGRATULATIONS! YOU SOLVED IT! 🎉")

            break



if __name__ == "__main__":

    main()