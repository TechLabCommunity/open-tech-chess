from itertools import product

from chess_piece import ChessPiece

X = ["a", "b", "c", "d", "e", "f", "g", "h"]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 8]


class King(ChessPiece):

    def __init__(self, pos_in_x, pos_in_y):
        super().__init__(pos_in_x, pos_in_y)

    def possible_poss(self):
        x, y = ord(self.pos_in_x), self.pos_in_y
        moves = list(product([x], [y - 1, y + 1])) + list(product([x - 1], [y - 1, y, y + 1])) \
                + list(product([x + 1], [y - 1, y, y + 1]))
        result_moves = []
        for x, y in moves:
            if ord('a') <= x <= ord('h') and 1 <= y <= 8:
                result_moves.append((chr(x), y))
        return print(result_moves)









