class ChessPiece:

    def __init__(self, x, y):
        if not (ord('a') <= ord(x) <= ord('h') and 1 <= y <= 8):
            raise ValueError(f"{x},{y} non sono coordinate valide.")
        self.pos_in_x = x
        self.pos_in_y = y

    # è possibile stampare qualsiasi pezzo con "print" perchè viene ereditato.
    def __str__(self):
        return f'{type(self)} : {self.pos_in_x}, {self.pos_in_y}'

    def possible_poss(self):
        raise NotImplementedError(f'{type(self)} non ha implementato possible_poss')
