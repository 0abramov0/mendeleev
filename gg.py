class TicTacToeBoard:
    def __init__(self):
        self.flag = True
        self.field = [['-'] * 3 for _ in range(3)]
        self.hodi = '-'
        self.end_flag = False

    def new_game(self):
        self.field = [['-'] * 3 for _ in range(3)]

    def get_field(self):
        return self.field

    def check_field(self):
        VAR_POBED = ((self.field[0][0], self.field[0][1], self.field[0][2]),
                     (self.field[1][0], self.field[1][1], self.field[1][2]),
                     (self.field[2][0], self.field[2][1], self.field[2][2]),
                     (self.field[0][0], self.field[1][0], self.field[2][0]),
                     (self.field[0][1], self.field[1][1], self.field[2][1]),
                     (self.field[0][2], self.field[1][2], self.field[2][2]),
                     (self.field[0][0], self.field[1][1], self.field[2][2]),
                     (self.field[0][2], self.field[1][1], self.field[2][0]))

    def make_move(self, row, col):
        if self.flag:
            if self.field[row - 1][col - 1] == '-':
                self.field[row - 1][col - 1] = 'X'
            else:
                return f'Клетка {row}, {col} уже занята'
            self.flag = False
        else:
            if self.field[row - 1][col - 1] == '-':
                self.field[row - 1][col - 1] = '0'
            else:
                return f'Клетка {row}, {col} уже занята'
            self.flag = True

        if not self.end_flag:
            return 'Продолжаем играть'
        else:
            return 'Игра уже завершенна'


board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
board.check_field()
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
