from itertools import product

from chess_piece import ChessPiece

X = ["a", "b", "c", "d", "e", "f", "g", "h"]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Bishop(ChessPiece):

    def __init__(self, pos_in_x, pos_in_y):
        super().__init__(pos_in_x, pos_in_y)

    def possible_poss(self):
        if self.pos_in_x not in X or self.pos_in_y not in Y:
            return print("x o y non esiste")
        x, y = ord(self.pos_in_x), self.pos_in_y
        finale_risult = []

        for n in range(1, 9):
            if n <= 8:
                count = 1
                moves = list(product([x + 1], [y + count]))
                for x, y in moves:
                    if ord('a') <= x <= ord('h') and 1 <= y <= 8:
                        finale_risult.append((chr(x), y))
                moves.clear()

        x = ord(self.pos_in_x)
        y = self.pos_in_y
        for n in range(1, 9):
            count = 1
            moves_1 = list(product([x - count], [y + count]))
            for x, y in moves_1:
                if ord('a') <= x <= ord('h') and 1 <= y <= 8:
                    finale_risult.append((chr(x), y))
            moves_1.clear()

        x = ord(self.pos_in_x)
        y = self.pos_in_y
        for n in range(1, 9):
            count = 1
            moves_2 = list(product([x - count], [y - count]))
            for x, y in moves_2:
                if ord('a') <= x <= ord('h') and 1 <= y <= 8:
                    finale_risult.append((chr(x), y))
            moves_2.clear()

        x = ord(self.pos_in_x)
        y = self.pos_in_y
        for n in range(1, 9):
            count = 1
            moves_3 = list(product([x + count], [y - count]))
            for x, y in moves_3:
                if ord('a') <= x <= ord('h') and 1 <= y <= 8:
                    finale_risult.append((chr(x), y))
            moves_3.clear()

        return finale_risult



