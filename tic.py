##Select Game Mode :
##    1. Single Player (v/s Computer)
##    2. Multi Player (v/s Player)

EMPTY = " "
X = "X"
O = "O"

def dis_instruct():
    """Display Game Instructions"""
    print("""
    Welcome To The Tic-Tac-Toe Game :

    You Will Make Your Move By Entering A Number(0-8)
    Corresponding To The Board Position.

    The Corresponding Positions Are:

            0 | 1 | 2
           ---+---+---
            3 | 4 | 5
           ---+---+---
            6 | 7 | 8

    So Let's Begin.
""")

def assign_symbol():
    """Assign Symbols to Player"""
    sym= None
    while sym not in ("O","X"):
        print("Please Select Your Symbol (O/X)")
        print("(Remember Always X Goes First!!)")
        sym = input("Symbol : ").upper()
    if sym == X:
        return X,O
    else:
        return O,X
        

def dis_board(board):
    """Display The Board"""
    print()
    print("\t ", board[0], "|", board[1], "|", board[2])
    print("\t", "---+---+---")
    print("\t ", board[3], "|", board[4], "|", board[5])
    print("\t", "---+---+---")
    print("\t ", board[6], "|", board[7], "|", board[8])
    print()

def move_hum(board):
    """Get Move From Human"""
    allowed_moves = []
    for x in range(9):
        if board[x] == EMPTY:
            allowed_moves.append(x)
    print(allowed_moves)
    move = None
    while move not in allowed_moves:
        move = int(input("Enter Your Move : "))
        if move not in allowed_moves:
            print("This Move Is Not Allowed,Choose Another : ")
    print("Done....")
    return move

def move_com(board,com,hum):
    """Get Move From Computer"""
    BESTM = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    b=board[:]
    allowed_moves = []
    for x in range(9):
        if board[x] == EMPTY:
            allowed_moves.append(x)
    for move in allowed_moves:
        b[move] = com
        if check_win(board) == com:
            return move
        b[move]=EMPTY
    for move in allowed_moves:
        b[move] = hum
        if check_win(board) == hum:
            return mov
        b[move]=EMPTY
    for move in BESTM:
        if move in allowed_moves:
            return move

def switch_turn(turn):
    """Switches Turn"""
    if turn == X:
        return O
    else:
        return X
    
def check_win(board):
    """Checks If Anyone Won The Game"""
    WINS = ((0, 1, 2),(3, 4, 5),(6, 7, 8),
            (0, 3, 6),(1, 4, 7),(2, 5, 8),
            (0, 4, 8),(2, 4, 6))
    for x in WINS:
        if board[x[0]] == board[x[1]] == board[x[2]] != EMPTY:
            return board[x[0]]
    if EMPTY not in board:
        return "TIE"
    return None

## main
dis_instruct()
hum, com = assign_symbol()
turn = X
board=[]
for x in range(9):
    board.append(EMPTY)
dis_board(board)
winner = None
while not winner:
    if turn == hum:
        move = move_hum(board)
        board[move] = hum
    else:
        move = move_com(board,com,hum)
        board[move] = com
    dis_board(board)
    turn = switch_turn(turn)
    winner = check_win(board)
if winner == hum:
    print("Congratulations You Won!!")
elif winner == com:
    print("Sorry, You Lost!!")
else:
    print("It Is A Tie!!")
    

