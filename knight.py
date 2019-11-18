from itertools import product

from chess_piece import ChessPiece

X = ["a", "b", "c", "d", "e", "f", "g", "h"]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Knight(ChessPiece):
    def __init__(self, pos_in_x, pos_in_y):
        super().__init__(pos_in_x, pos_in_y)

    def pos_knight(self):
        if self.pos_in_x not in X or self.pos_in_y not in Y:
            return print("x o y non esiste")
        x, y = ord(self.pos_in_x), self.pos_in_y
        moves = list(product([x - 1, x + 1], [y - 2, y + 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
        result_moves = []
        for x, y in moves:
            if ord('a') <= x <= ord('h') and 1 <= y <= 8:
                result_moves.append((chr(x), y))

        return print(result_moves)











