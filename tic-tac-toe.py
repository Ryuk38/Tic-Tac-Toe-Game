print("\t\t\tTic-tac-toe")
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
winner = None
game_running = True

# creating the board


def printBoard(board):
    print("---------")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")


# taking input from user
def playerInput(board):
    inp = int(input("Enter a number between 1-9:"))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("Oops position already occupied!!")

# check for horizontal win


def horizontal_win(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# check for row win


def row_win(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

# check for diagonal win


def diag_win(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# to check for a tie


def check_tie(board):
    global game_running
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        game_running = False

# to check for win


def check_win():
    global game_running
    if diag_win(board) or row_win(board) or horizontal_win(board):
        printBoard(board)
        print(f"The winner is {winner}")
        game_running = False


# switch the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# game loop
while game_running:
    printBoard(board)
    playerInput(board)
    check_win()
    check_tie(board)
    switch_player()


