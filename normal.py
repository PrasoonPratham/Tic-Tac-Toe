# Board
board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' '}

# Player turn
turn = 'X'

# Count
c = 0

# Draw the board
def draw():
    print(board[7], "|" ,board[8], "|" ,board[9])
    print("---------")
    print(board[4], "|" ,board[5], "|" ,board[6])
    print("---------")
    print(board[1], "|" ,board[2], "|" ,board[3])

def game():
    input("")
