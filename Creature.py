import Chromosome

class Creature:

    def __init__(self):
        self.genome = Chromosome()
        self.player = 1
        self.record = (0,0)

    def assign_num(self, num):
        self.player_num = num

    def mate(self, other):

    def make_move(self, board):
