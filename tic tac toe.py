# add Tkinter module
import tkinter as tk

# 1. Create the main window
root = tk.Tk()

# 2. Set window properties
root.title("Tic Tac Toe Game")
root.geometry("300x200")

# 3. Add widgets
label = tk.Label(root, text="Welcome!")

# 4. Arrange widgets
label.pack(pady = 10)

# 5. Enter the main event loop
root.mainloop()

size = input("Print the size of board: ")
board = []

# create board array for board
def create_board(size):
    i = 0
    while(i < size):
        board.append([])
        j = 0
        while(j < size):
            board[i].append(' ')
            j = j + 1
        i = i + 1
        
# print board array
def print_board(size):
    i = 0
    while(i < size):
        j = 0
        while(j < size):
            if board[i][j] == " ":
                print("__|", end="")
            else:
                print(board[i][j], end="|")
            j = j + 1
        print("\n")
        i = i + 1

# map coordinates and print marker
def map_coordinates(marker):
    row = input("Enter row coordinates: ")
    col = input("Enter col coordinates: ")

    # validate inputs
    if row.isdigit() and col.isdigit():
        if int(row) - 1 in range(0, int(size) - 1) and int(col) - 1 in range(0, int(size) - 1):
            if board[int(row) - 1][int(col) - 1] == " ":
                board[int(row) - 1][int(col) - 1] = marker
                print_board(int(size))
        else:
            print("Enter valid coordinates")
            return []
    else:
        print("Enter valid coordinates")
        return []

    return [row, col]

# check for row win
def check_row_win(row):
    is_win = False
    
    j = 0
    while(j < int(size)):
        if board[row - 1][j] == "X" or board[row - 1][j] == "O":
            while j + 1 <= int(size) - 1 and board[row - 1][j] == board[row - 1][j + 1]:
                if (j + 1 == int(size) - 1):
                    print("row win")
                    is_win = True     
                j += 1
        return is_win 
        

# check for col win
def check_col_win(col):
    i = 0
    is_win = False
    while(i < int(size)):
        if board[i][col - 1] == "X" or board[i][col - 1] == "O":
            while i + 1 <= int(size) - 1 and board[i][col - 1] == board[i + 1][col - 1]:
                if (i + 1 == int(size) - 1):
                    print("col win")
                    is_win = True
                i += 1
        return is_win
        

# check for diagonal win
def check_diagonal_win(pos):
    is_win = False
    if int(pos[0]) == int(pos[1]):
        i = 0
        while(i < int(size)):
            while i + 1 <= int(size) - 1 and board[i][i] != " " and board[i][i] == board[i + 1][i + 1]:
                if (i + 1 == int(size) - 1):
                    print("diagonal win")
                    is_win = True
                i += 1
            return is_win
    elif int(pos[0]) + int(pos[1]) == int(size) + 1:
        i = 0
        while i < int(size):
            j = int(size) - 1
            while j >= 0:
                while i + 1 <= int(size) - 1 and j - 1 >= 0 and board[i][j] == board[i + 1][j - 1]:
                    if (i + 1 == int(size) - 1 and j - 1 == 0):
                        print("diagonal win")
                        is_win = True
                    j -= 1
                    i += 1
                is_win = False
                return is_win
        return is_win

# check for all kinds of wins
def check_win(pos):
    if check_row_win(int(pos[0])) == True or check_col_win(int(pos[1])) == True or check_diagonal_win(pos) == True:
        return True
    
# check for draw
def check_draw(is_win):
    is_draw = False
    i = 0
    while i < int(size):
        j = 0
        while j < int(size):
            if board[i][j] != " " and is_win == False:
                is_draw = False 
                return is_draw
            j += 1
        i += 1
        is_draw = True
    return is_draw

# play game
def play_game():
    is_playing = True
    player_1 = True
    marker = "X"
    position = []
    is_draw = False
    while is_playing:
        if player_1 == True:
            marker = "X"
            player_1 = False
        else:
            marker = "O"
            player_1 = True
        position = map_coordinates(marker)
        if len(position) != 0:
            if check_win(position) == True:
                is_playing = False
            else:
                is_draw = check_draw(False)
                if is_draw == True:
                    print("Game draw")
                    is_playing = False

# start game
def start_game():
    if int(size) >= 3:
        create_board(int(size))
        print_board(int(size))
        play_game()
    else:
        print("size is not correct")

start_game()