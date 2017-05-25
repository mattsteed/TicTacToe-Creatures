# This is the main program for the game

import Players as P
import Game as G
import Trainer as T


def train_bot(bot):
  bot = T.self_train(bot, 70000, gamma=0.9, lr=0.0001)
  print()
  bot = T.self_train(bot, 50000, gamma=0.9, lr=0.00005)
  print()
  return bot


if __name__=='__main__':
  print("This is tic tac toe.")

  print("What type of player would you like to play against?")
  print("0: A random player")
  print("1: Another human")
  print("2: A bot that learns")
  choice = int(input("Enter the number for your choice: "))

  while ((choice != 0) and (choice != 1) and (choice != 2)):
    choice = int(input("Invalid choice. Choose again: "))
    

  human = P.Human_Player()
  if (choice == 0):
    opponent = P.Random_Player()
  elif (choice == 1):
    opponent = human
  elif (choice == 2):
    opponent = P.QLearner()

  while (1):
    if (choice == 2):
      train_choice = int(input("Would you like to train the bot? (0/1): "))
      if train_choice:
        opponent = train_bot(opponent)
    player_choice = int(input("What player do you want to be? (1/2): "))
    print("The game begins now")
    if (player_choice == 1):
      winner = G.play_game(human, opponent)
    else:
      winner = G.play_game(opponent, human)
    if (winner == 0):
      print("No one wins.")
    else:
      print("The winner is player {}.".format(winner))
    print()



