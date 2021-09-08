import sys

# Board
board = {7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' '}

# Player turn
turn = 'X'

# Count
count = 0

# Draw the board
def draw():
    print(board[7], "|" ,board[8], "|" ,board[9])
    print("--+---+--")
    print(board[4], "|" ,board[5], "|" ,board[6])
    print("--+---+--")
    print(board[1], "|" ,board[2], "|" ,board[3])

# Main loop
def game():

    # Global variables
    global count, turn

    # Checking to see if the player has won
    def checkwin():
        global count, turn
        if board[1] == board[2] == board[3] == turn:
            print("Player ", turn, " wins!")
            sys.exit()
        elif board[4] == board[5] == board[6] == turn:
            print("Player ", turn, " wins!")
            sys.exit()
        elif board[7] == board[8] == board[9] == turn:
            print("Player ", turn, " wins!")
            sys.exit()
        elif board[1] == board[4] == board[7] == turn:
            print("Player ", turn, " wins!")
            sys.exit()
        elif board[2] == board[5] == board[8] == turn:
            print("Player ", turn, " wins!")
            sys.exit()
        elif board[3] == board[6] == board[9] == turn:
            print("Player ", turn, " wins!")
            sys.exit()
        elif board[1] == board[5] == board[9] == turn:
            print("Player ", turn, " wins!")
            sys.exit()
        elif board[3] == board[5] == board[7] == turn:
            print("Player ", turn, " wins!")
            sys.exit()
            
    # Play until the game is over
    while count<10:
        checkwin()
        if count % 2 == 0:
            ans = int(input("Player X, which place would you like to place your move? "))
            if ans < 10 and ans > 0:
                if board[ans] == ' ':
                    board[ans] = 'X'
                    count += 1
                    draw()
                else:
                    print("That place is already taken!")
                    game()
            else:
                print("Please enter a number between 1 and 9!")
                game()

        elif count % 2 == 1:
            ans = int(input("Player O, which place would you like to place your move? "))
            if ans < 10 and ans > 0:
                if board[ans] == ' ':
                    board[ans] = 'O'
                    count += 1
                    draw()
                else:
                    print("That place is already taken!")
                    game()
            else:
                print("Please enter a number between 1 and 9!")
                game()

    #Tie
    else:
        print("It's a tie!")
    
game()



