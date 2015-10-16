import random

class Chromosome:
    
    def __init__(self):
        self.chromosome = [random.randint(0,25) for i in range(100)]

    def cross_over(self, other):
        break_1 = random.randint(0,len(self.chromosome) - 1)
        break_2 = random.randint(0,len(self.chromosome) - 1)
        break_3 = random.randint(0,len(other.chromosome) - 1)
        break_4 = random.randint(0,len(other.chromosome) - 1)
        if break_1 > break_2:
            break_1 = break_1 + break_2
            break_2 = break_1 - break_2
            break_1 = break_1 - break_2
        if break_4 > break_3:
            break_3 = break_3 + break_4
            break_4 = break_3 - break_4
            break_3 = break_3 - break_4


    def mutate(self):
        for i in range(len(self.chromosome)):
            test = random.randint(0,200)
            if test <= 5:
                self.chromosome[i] = random.randint(0,25)










