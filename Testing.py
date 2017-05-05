from TicTacToe import *
import Creature

x = TicTacToe()

x.add_X(1)
x.add_X(5)
x.add_O(4)
x.add_X(9)
print(x.board)
print(str(x.check_for_win(1)))
print(x.main_dic[1])
x.print_board()
y = Creature.Creature()
print y.genome.chromosome