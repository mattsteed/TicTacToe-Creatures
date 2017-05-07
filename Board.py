class TicTacToe:

    main_dic = {0:' ', 1:'X', 2:'O'}

    def __init__(self):
        self.board = [0 for i in range(9)]

    def add_X(self, position):
        if self.board[position - 1] != 0:
            return 0
        else:
            self.board[position - 1] = 1
            return 1

    def add_O(self, position):
        if self.board[position - 1] != 0:
            return 0
        else:
            self.board[position - 1] = 2
            return 1

    def check_for_win(self, player_num):
        for i in range(0,7,3):
            if (self.board[i] == player_num and \
                self.board[i] == self.board[i + 1]) and \
                (self.board[i + 1] == self.board[i + 2]):
                return 1
        for i in range(3):
            if (self.board[i] == player_num and \
                self.board[i] == self.board[i + 3]) and \
                (self.board[i + 3] == self.board[i + 6]):
                return 1
        if (self.board[0] == player_num and \
            self.board[0] == self.board[4]) and \
                (self.board[4] == self.board[8]):
                return 1
        if (self.board[0] == player_num and \
            self.board[2] == self.board[4]) and \
                (self.board[4] == self.board[6]):
                return 1
        return 0

    def print_board(self):
        print(' ' + self.main_dic[self.board[0]] + ' | ' + \
            self.main_dic[self.board[1]] + ' | ' + self.main_dic[self.board[2]])
        print('-----------')
        print(' ' + self.main_dic[self.board[3]] + ' | ' + \
            self.main_dic[self.board[4]] + ' | ' + self.main_dic[self.board[5]])
        print('-----------')
        print(' ' + self.main_dic[self.board[6]] + ' | ' + \
            self.main_dic[self.board[7]] + ' | ' + self.main_dic[self.board[8]])


