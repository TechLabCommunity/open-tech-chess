from chess_piece import ChessPiece

X = ["a", "b", "c", "d", "e", "f", "g", "h"]
Y = [1, 2, 3, 4, 5, 6, 7, 8]


class Rook(ChessPiece):

    def __init__(self, pos_in_x, pos_in_y):
        super().__init__(pos_in_x, pos_in_y)

    def pos_rook(self):
        x, y = ord(self.pos_in_x), self.pos_in_y
        if self.pos_in_y not in Y or self.pos_in_x not in X:
            print("Non esiste x oppure y.")

        else:
            result_moves = []
            for element_x in X:
                if self.pos_in_x != element_x:
                    result_moves.append((element_x, self.pos_in_y))
                elif self.pos_in_x == element_x:
                    for element_y in Y:
                        if element_y != self.pos_in_y:
                            result_moves.append((self.pos_in_x, element_y))
            return print(result_moves)




