# File with class definitions of players for tic tac toe

import numpy as np
import NeuralNet as nn
import sys


class Player:
  def __init__(self, num_hidden=18):
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
    


class QLearner(Player):
  def __init__(self, num_hidden=18):
    self.model = nn.NeuralNet()
    self.model.add_layer(nn.HiddenLayer(9, num_hidden))
    self.model.add_layer(nn.ReluLayer())
    self.model.add_layer(nn.HiddenLayer(num_hidden, 9))
    self.sq = nn.SquaredLoss()

  def make_move(self, board, player_num): 
    board_ = board.board
    multiplier = -2 * player_num + 3
    output = self.model.forward(multiplier*board_.reshape(1,9))
    move = np.argmax((output - np.min(output)) * (board_.reshape(1,9) == 0))
    board.make_move(move, player_num)
    return output, move

  def get_move(self, board, player_num):
    multiplier = -2 * player_num + 3
    output = self.model.forward(multiplier*board_.reshape(1,9))
    return output
    

  def update(self, player_num, input, label, learning_rate=0.01, weight_decay=0):
    N = input.size
    multiplier = -2 * player_num + 3
    output = self.model.forward(multiplier*input.reshape(1,N))
    self.sq.forward(output.reshape(1,N), label.reshape(1,N))
    grad_out = self.sq.back_prop(label.reshape(1,N))
    self.model.back_prop(grad_out, learning_rate, weight_decay)

  def __str__(self):
    return "Q learner"
