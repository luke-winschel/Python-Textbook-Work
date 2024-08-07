#Two player, two dimensional tic-tac-toe.  Write a script to play two player tic-tac-toe, using a 3x3 array

import numpy as np

#establish a board
list = np.array([x for x in range (1,10,1)])
board = ['1',' ',' ',' ',' ',' ',' ',' ',' ']

def play_game():
    print (list.reshape(3,3))
    
    player1_selection = int(input("Please select a location! "))
    pl1_update_board(player1_selection)
    print(list.reshape (3,3))
    #check_win()

    #player2_selection = input("Please select a location! ")
    #pl2_update_board(player2_selection)
    #check_win()

def pl1_update_board(player1_selection):
    if board[player1_selection] != ' ':
        print('Spot is taken! Try Again!')
    else:
        board[player1_selection] = 'X'
    return board


def pl2_update_board(player2_selection):
   O = board[player2_selection - 1]
   if O != board[O]:
       print("Spot is taken! Try again!")
   else:
       board[O] = 'O'
       
print ("Player 1 will be X's and player 2 will be O's")
print (board)
play_game()