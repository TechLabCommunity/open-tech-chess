class Chess:

    def __init__(self):
        # inizialmente la scacchiera non ha pezzi.
        self.pieces = []

    # static perchè non elabora campi self.
    @staticmethod
    def __check_pos(x, y):
        # x dovrebbe essere una lettera
        # se x non è una lettera valida e nemmeno y un numero valido...
        if not (ord('a') <= ord(x) <= ord('h') and 0 <= y <= 7):
            raise ValueError(f"{x},{y} non sono coordinate valide.")

    def __check_conflict_position(self, new_piece):
        # rimuovo i pezzi che hanno le stesse caselle del nuovo pezzo. Non possono esistere due pezzi nella stessa casella.
        self.pieces = list(filter(lambda p: p.pos_in_x != new_piece.pos_in_x and p.pos_in_y != new_piece.pos_in_y, self.pieces))



    def set_piece(self, piece_actual):
        self.__check_pos(piece_actual.pos_in_x, piece_actual.pos_in_y)
        self.__check_conflict_position(piece_actual)
        # se va tutto bene aggiungo il pezzo.
        self.pieces.append(piece_actual)
        # ritorno i pezzi sulla scacchiera per comodità. Non è obbligatorio.
        return self.pieces

    def __str__(self):
        s = "Pezzi sulla scacchiera : \n"
        for p in self.pieces:
            s += str(p)+"\n"
        return s
