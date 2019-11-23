from itertools import product

from chess_piece import ChessPiece

X = ["a", "b", "c", "d", "e", "f", "g", "h"]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# sarebbe stato meglio fare così per tutti i pezzi. Alla fine tutte le pedine hanno pos x e pos y.
# Conviene sempre ereditare se le classi hanno campi in comune!!!


class Pawn(ChessPiece):

    def __init__(self, pos_in_x, pos_in_y):
        super().__init__(pos_in_x, pos_in_y)

    def possible_poss(self):
        x, y = ord(self.pos_in_x), self.pos_in_y
        if self.pos_in_y not in Y or self.pos_in_x not in X:
            print("Non esiste x oppure y.")

        if self.pos_in_y == 2:
            moves = list(product([x], [y + 1, y + 2]))
            result_moves = []
            for x, y in moves:
                if ord('a') <= x <= ord('h'):
                    result_moves.append((chr(x), y))
            return print(result_moves)
        elif self.pos_in_y == 8:
            print("Puoi cambiare il pedone per qualcuno")

        else:
            moves = list(product([x], [y + 1]))
            result_moves = []
            for x, y in moves:
                if ord('a') <= x <= ord('h') and 1 <= y <= 8:
                    result_moves.append((chr(x), y))
            return print(result_moves)
