class ChessPiece:

    def __init__(self, x, y):
        if not (ord('a') <= ord(x) <= ord('h') and 0 <= y <= 7):
            raise ValueError(f"{x},{y} non sono coordinate valide.")
        self.pos_in_x = x
        self.pos_in_y = y
