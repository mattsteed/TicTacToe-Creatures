# File with class definitions of players for tic tac toe

import numpy as np
import NeuralNet as nn
import sys


class Player:
  def __init__(self):
    pass

  def make_move(self, board, player_num):
    pass

#  def get_player_num(self):
#    return self.player_num


class Human_Player(Player):
  def make_move(self, board, player_num):
    print("You are player {}.".format(player_num))
    print("The current board is:")
    board.print_board()
    move = int(input("Pick an index to play: "))
    while not (board.make_move(move, player_num)):
      print("That move is invalid. Try again.")
      move = int(input("Pick another index to play: "))

  def __str__(self):
    return "Human player"

    

class Random_Player(Player):
  def make_move(self, board, player_num):
    moves = np.random.permutation(9)
    for move in moves:
      if (board.make_move(move, player_num)):
        return 

  def __str__(self):
    return "Random player"
    

