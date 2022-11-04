from IPython.display import clear_output
import random
from termcolor import colored
from time import sleep
 
def display_board(board):
    clear_output()        #This line clears the previous output everytime you run the code
    k = len(board)-1
    for i in range(3):
        print('     |     |')
        print(' ',board[k-2],' | ',board[k-1],' | ',board[k])
        print('     |     |')
        if i==2:
            break
        else:
            print('------------------')
        k -= 3
 
def player_input():
    marker = input('Player 1 choose either x or o: ').upper()
    while marker!='X' and marker!='O':
        clear_output()
        marker = input("wrong input! choose either 'x' or 'o': ").upper()
    clear_output()
    if marker=="X":
        return ('X','O')
    else:
        return ('O','X')
 
def place_marker(board, marker, position):
    board[position] = marker
 
def win_check(board,mark):
  # check all the rows
  decision = False
  i = 1
  while i in range(1,8):
    if board[i]==board[i+1]==board[i+2]==mark:
      board[i] = colored(board[i],'red')
      board[i+1] = colored(board[i+1],'red')
      board[i+2] = colored(board[i+2],'red')
      decision = True
    i+=3
  # check all the columns
  for i in range(1,4):
    if board[i]==board[i+3]==board[i+6]==mark:
      board[i] = colored(board[i],'red')
      board[i+3] = colored(board[i+3],'red')
      board[i+6] = colored(board[i+6],'red')
      decision = True
  # check the diagonals
  for i in range(1,4):
    if i==1:
      if board[i]==board[i+4]==board[i+8]==mark:
        board[i] = colored(board[i],'red')
        board[i+4] = colored(board[i+4],'red')
        board[i+8] = colored(board[i+8],'red')
        decision = True
    else:
      if board[i]==board[i+2]==board[i+4]==mark:
        board[i] = colored(board[i],'red')
        board[i+2] = colored(board[i+2],'red')
        board[i+4] = colored(board[i+4],'red')
        decision = True
    i+=2
  return decision
 
def choose_first():
  flip = random.randint(0,1)
  if flip == 0:
    return "Player 1"
  else:
    return "Player 2"
 
#review the next two methods. They can be done in one
def space_check(board, position):       
  return board[position]== ' '
 
def full_board_check(board):
  for i in range(1,10):
    if space_check(board,i):
      return False
  return True
 
def Player_choice(board):
  position = 0
  items = [1,2,3,4,5,6,7,8,9]
  while position not in items or not space_check(board,position):
    position = int(input('Choose a position [from 1 to 9]: '))
  return position 
 
def replay():
  replay = input("Would you like to play again?[y/n] :")
  return replay.lower() == 'y'
 
print('Welcome to Tic-Tac-Toe!! ')
print("Your numpad represents the board in the game")
 
while True:
  ##Set everything up
  board = [" "]*10
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  print(turn+" Goes First!")
  play_game = input("Ready to play?[y/n]: ")
  if play_game.lower()== 'y':
    game_on = True
  else:
    game_on = False
 
  ##Gameplay
  while game_on:
    if turn == 'Player 1':
    ##Player 1 turn
      ##show the board
      display_board(board)
      ##choose a position
      position = Player_choice(board)
      ##place a marker on the position
      place_marker(board,player1_marker,position)
      ##check if he won
      if win_check(board,player1_marker):
        display_board(board)
        print('Player 1 has won!')
        game_on = False
      else:
        if full_board_check(board):
          display_board(board)
          print("It's a tie!")
          game_on = False
        else:
          turn = 'Player 2'
 
    else:
    ##Player 2 turn
      ##show the board
      display_board(board)
      ##choose a position
      position = Player_choice(board)
      ##place a marker on the position
      place_marker(board,player2_marker,position)
      ##check if he won
      if win_check(board,player2_marker):
        display_board(board)
        print('Player 2 has won!')
        game_on = False
      else:
        if full_board_check(board):
          display_board(board)
          print("It's a tie!")
          game_on = False
        else:
          turn = 'Player 1'
 
  if replay() == True:
    print("Okay then, let's play again!!")
  else:
    clear_output()
    print("Thanks for playing!!")
    sleep(2)  #the program goes to sleep for 2 seconds before executing the next line
    clear_output()
    break