# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check for a win
def check_win():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    
    return False

# Function to play the game
def play_game():
    print("Let's play Tic Tac Toe!")
    print_board()
    player = 'X'
    
    while True:
        position = int(input("Enter position (1-9): ")) - 1
        
        if board[position] == ' ':
            board[position] = player
            print_board()
            
            if check_win():
                print("Player", player, "wins!")
                break
            
            if ' ' not in board:
                print("It's a tie!")
                break
            
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")
        
# Start the game
play_game()
