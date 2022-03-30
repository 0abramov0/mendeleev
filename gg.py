class TicTacToeBoard:
    def __init__(self):
        self.flag = True

    def new_game(self):
        self.field = [['-'] * 3 for _ in range(3)]


    def get_field(self):
        return self.field

    def make_mowe(self, row, col):
        if self.flag:
            if self.field[row][col] == '-':
                self.field[row][col] = 'X'
            else:
                return f'Клетка {row}, {col} уже занята'
            self.flag = False
        else:
            if self.field[row][col] == '-':
                self.field[row][col] = '0'
            else:
                return f'Клетка {row}, {col} уже занята'
            self.flag = True



tictac = TicTacToeBoard()
tictac.new_game()
print(*tictac.get_field(), sep='\n')