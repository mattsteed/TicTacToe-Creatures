# File with code to play a game of tic tac toe

import numpy as np
import Board as B
import Players as P

def play_game(p1, p2, verbose=0):
  board = B.Board()
  if (verbose):
    print("Starting game. The players are:")
    print(p1)
    print(p2)
    print("Player 1 moving:")

  for i in range(4):
    p1.make_move(board, 1)
    if (verbose):
      print("The board is:")
      board.print_board()
    if (board.check_for_win(1)):
      if (verbose):
        print("Player 1 wins.")
      return 1
    if (verbose):
      print("Player 2 moving:")

    p2.make_move(board, 2)
    if (verbose):
      print("The board is:")
      board.print_board()
    if (board.check_for_win(2)):
      if (verbose):
        print("Player 2 wins.")
      return 2
    if (verbose):
      print("Player 1 moving:")

  p1.make_move(board, 1)
  if (verbose):
    print("The board is:")
    board.print_board()
  if (board.check_for_win(1)):
    if (verbose):
      print("Player 1 wins.")
    return 1
  
  if (verbose):
    print("No one wins.")
  return 0
