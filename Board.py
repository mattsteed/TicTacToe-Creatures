# File with definition of game board

import numpy as np

class Board:
  print_dict = {0:' ', 1:'X', 2:'O'}
  def __init__(self):
    self.board = np.zeros(9)

  def make_move(self, move, player_num):
    if not (0 <= move and move <= 8):
      return 0
    if not (player_num == 1 or player_num == 2):
      return 0
    if self.board[move] != 0:
      return 0
    self.board[move] = player_num
    return 1

  """
  def add_O(self, position):
    if not (0 <= position and position <= 8):
      return 0
    if self.board[position] != 0:
      return 0
    else:
      self.board[position] = 2
      return 1
  """

  def check_for_win(self, player_num):
    for i in range(0,7,3):
      if (self.board[i] == player_num and \
          self.board[i + 1] == player_num and \
          self.board[i + 2] == player_num):
        return 1
    for i in range(3):
      if (self.board[i] == player_num and \
          self.board[i + 3] == player_num and \
          self.board[i + 6] == player_num):
        return 1
    if (self.board[0] == player_num and \
        self.board[4] == player_num and \
        self.board[8] == player_num):
      return 1
    if (self.board[2] == player_num and \
        self.board[4] == player_num and \
        self.board[6] == player_num):
      return 1
    return 0

  def print_board(self):
    print(' ' + self.print_dict[self.board[0]] + ' | ' + \
      self.print_dict[self.board[1]] + ' | ' + self.print_dict[self.board[2]])
    print('-----------')
    print(' ' + self.print_dict[self.board[3]] + ' | ' + \
      self.print_dict[self.board[4]] + ' | ' + self.print_dict[self.board[5]])
    print('-----------')
    print(' ' + self.print_dict[self.board[6]] + ' | ' + \
      self.print_dict[self.board[7]] + ' | ' + self.print_dict[self.board[8]])

  def clear(self):
    self.board = np.zeros(9)



