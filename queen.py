from bishop import Bishop
X = ["a", "b", "c", "d", "e", "f", "g", "h"]
Y = [1, 2, 3, 4, 5, 6, 7, 8]


class Queen(Bishop):
    def __init__(self, pos_in_x, pos_in_y):
        super().__init__(pos_in_x, pos_in_y)

    def actual_position(self):
        return self.pos_in_x, self.pos_in_y

    def possible_poss(self):
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
            return result_moves

