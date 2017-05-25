# File with definition of game board

import numpy as np

class Board:
  print_dict = {0:' ', 1:'X', -1:'O'}
  def __init__(self):
    self.board = np.zeros(9)

  def make_move(self, move, player_num):
    if not (0 <= move and move <= 8):
      return 0
    if not (player_num == 1 or player_num == 2):
      return 0
    if self.board[move] != 0:
      return 0
    # This maps 1 to 1 and 2 to -1
    self.board[move] = -2 * player_num + 3
    return 1

  def clear_move(self, move):
    self.board[move] = 0

  def check_for_win(self, player_num):
    for i in range(0,7,3):
      if (self.board[i] == (-2*player_num + 3) and \
          self.board[i + 1] == (-2*player_num + 3) and \
          self.board[i + 2] == (-2*player_num + 3)):
        return 1
    for i in range(3):
      if (self.board[i] == (-2*player_num + 3) and \
          self.board[i + 3] == (-2*player_num + 3) and \
          self.board[i + 6] == (-2*player_num + 3)):
        return 1
    if (self.board[0] == (-2*player_num + 3) and \
        self.board[4] == (-2*player_num + 3) and \
        self.board[8] == (-2*player_num + 3)):
      return 1
    if (self.board[2] == (-2*player_num + 3) and \
        self.board[4] == (-2*player_num + 3) and \
        self.board[6] == (-2*player_num + 3)):
      return 1
    return 0

  def check_if_full(self):
    if (np.sum(self.board==0)):
      return 0
    return 1

  def get_board(self):
    return self.board

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


# This function returns a board with a random, valid configuration
def get_random_board():
  board = Board()
  moves = np.random.permutation(9)
  num_moves = np.random.randint(0, 9)
  for i in range(num_moves):
    board.make_move(moves[i], i%2+1)
  while (board.check_for_win(1) or board.check_for_win(2)):
    board.clear()
    moves = np.random.permutation(9)
    num_moves = np.random.randint(0, 7)
    for i in range(num_moves):
      board.make_move(moves[i], i%2+1)
  return board
      
