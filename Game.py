# File with code to play a game of tic tac toe

import numpy as np
import Board as B
import Players as P


def play_game(p1, p2, verbose=0):
  board = B.Board()
  players = [p1, p2]

  if (verbose):
    print("Starting game. The players are:")
    print(p1)
    print(p2)

  for i in range(9):
    curr_player = i%2 + 1
    if (verbose):
      print("Player {} moving:".format(curr_player))

    players[curr_player-1].make_move(board, curr_player)
    if (verbose):
      print("The board is:")
      board.print_board()
    if (board.check_for_win(curr_player)):
      if (verbose):
        print("Player {} wins.".format(curr_player))
      return curr_player
 
  if (verbose):
    print("No one wins.")
  return 0
