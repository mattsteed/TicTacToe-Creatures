# Code for training a QLearner player to play

import numpy as np
import Board as B
import Players as P
import Game as G
from copy import copy,deepcopy


def update_learner(learner, board, output, move, player_num, gamma, lr):
  win_r = 2
  loss_r = -5
  if (player_num == 1):
    cat_r = 0
  elif (player_num == 2):
    cat_r = 2

  opp_num = 3-player_num
  label = copy(output)

  if (board.check_for_win(player_num)):
    label[0][move] = win_r
    board.clear_move(move)
    learner.update(player_num,board.get_board(),label,learning_rate=lr) 
    board.make_move(move, player_num)
    return

  if (board.check_if_full()):
    label[0][move] = cat_r 
    board.clear_move(move)
    learner.update(player_num,board.get_board(),label,learning_rate=lr) 
    board.make_move(move, player_num)
    return

  _,opp_move = learner.make_move(board, opp_num)

  if (board.check_for_win(opp_num)):
    label[0][move] = loss_r
    board.clear_move(move)
    board.clear_move(opp_move)
    learner.update(player_num,board.get_board(),label,learning_rate=lr) 
    board.make_move(move, player_num)
    return
  if (board.check_if_full()):
    label[0][move] = cat_r
    board.clear_move(move)
    board.clear_move(opp_move)
    learner.update(player_num,board.get_board(),label,learning_rate=lr) 
    board.make_move(move, player_num)
    return

  new_output,new_move = learner.make_move(board, player_num)
  label[0][move] = gamma*new_output[0][new_move]
    
  board.clear_move(move)
  board.clear_move(opp_move)
  board.clear_move(new_move)

  learner.update(player_num,board.get_board(),label,learning_rate=lr)

  # return the board to its original state
  board.make_move(move, player_num)
  return 
    
   

# This function trains a QLearner player for a single game
def self_train_single(learner, gamma=0.9, lr=0.01):
  board = B.Board()

  for i in range(4):
    output, move = learner.make_move(board, 1)
    update_learner(learner, board, output, move, 1, gamma, lr)
    if (board.check_for_win(1)):
      return 1

    output, move = learner.make_move(board, 2)
    update_learner(learner, board, output, move, 2, gamma, lr)
    if (board.check_for_win(2)):
      return 2

  output, move = learner.make_move(board, 1)
  update_learner(learner, board, output, move, 1, gamma, lr)
  if (board.check_for_win(1)):
    return 1
  
  return 0


# This function tests the perfomance of the leaner against a random player
def rand_val(ql, num_games=100):
  rand = P.Random_Player()
  """
  num_wins = 0
  num_cats = 0
  num_losses = 0
  """

  num_wins_1 = 0
  num_cats_1 = 0
  num_losses_1 = 0
  num_wins_2 = 0
  num_cats_2 = 0
  num_losses_2 = 0



  for i in range(int(num_games/2)):
    result = G.play_game(ql, rand)
    if (result == 0):
      num_cats_1 += 1
      continue
    if (result == 1):
      num_wins_1 += 1
      continue
    if (result == 2):
      num_losses_1 += 1

  for i in range(int(num_games/2)):
    result = G.play_game(rand, ql)
    if (result == 0):
      num_cats_2 += 1
      continue
    if (result == 1):
      num_losses_2 += 1
      continue
    if (result == 2):
      num_wins_2 += 1
  
  """
  wp = num_wins / num_games
  lp = num_losses / num_games
  cp = num_cats / num_games
  """

  wp1 = num_wins_1 / int(num_games/2)
  lp1 = num_losses_1 / int(num_games/2)
  cp1 = num_cats_1 / int(num_games/2)
  wp2 = num_wins_2 / int(num_games/2)
  lp2 = num_losses_2 / int(num_games/2)
  cp2 = num_cats_2 / int(num_games/2)

  return ((wp1, lp1, cp1), (wp2, lp2, cp2))
  #return (wp, lp, cp)


# This function tests the perfomance of the leaner against another player 
def opp_val(ql, opp, num_games=100):
  num_wins_1 = 0
  num_cats_1 = 0
  num_losses_1 = 0
  num_wins_2 = 0
  num_cats_2 = 0
  num_losses_2 = 0

  for i in range(int(num_games/2)):
    result = G.play_game(ql, opp)
    if (result == 0):
      num_cats_1 += 1
      continue
    if (result == 1):
      num_wins_1 += 1
      continue
    if (result == 2):
      num_losses_1 += 1

  for i in range(int(num_games/2)):
    result = G.play_game(opp, ql)
    if (result == 0):
      num_cats_2 += 1
      continue
    if (result == 1):
      num_losses_2 += 1
      continue
    if (result == 2):
      num_wins_2 += 1
  
  wp1 = num_wins_1 / int(num_games/2)
  lp1 = num_losses_1 / int(num_games/2)
  cp1 = num_cats_1 / int(num_games/2)
  wp2 = num_wins_2 / int(num_games/2)
  lp2 = num_losses_2 / int(num_games/2)
  cp2 = num_cats_2 / int(num_games/2)

  return ((wp1, lp1, cp1), (wp2, lp2, cp2))




def self_train(learner, num_games, gamma=0.9, lr=0.01):
  print("Training a learner for {} games with gamma = {} and a learning rate of {}"\
        .format(num_games, gamma, lr))
  val_freq = 500
  for i in range(num_games):
    self_train_single(learner, gamma, lr)
    if (i % 500 == 0):
      print("After {} training games, the win/loss/cat ratio against a random opponent is:".format(i))
      print(rand_val(learner,num_games=500))


def self_train_opp(learner, opp, num_games, gamma=0.9, lr=0.01):
  print("Training a learner for {} games with gamma = {} and a learning rate of {}"\
        .format(num_games, gamma, lr))
  val_freq = 500
  for i in range(num_games):
    self_train_single(learner, gamma, lr)
    if (i % 500 == 0):
      print("After {} training games, the win/loss/cat ratio against a chosen opponent is:".format(i))
      print(opp_val(learner,opp,num_games=10))



