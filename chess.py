class Chess:

    def __init__(self):
        # inizialmente la scacchiera non ha pezzi.
        self.pieces = []

    # static perchè non elabora campi self.
    @staticmethod
    def __check_pos(x, y):
        # x dovrebbe essere una lettera
        # se x non è una lettera valida e nemmeno y un numero valido...
        if not (ord('a') <= ord(x) <= ord('h') and 1 <= y <= 8):
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
        s = "Pezzi sulla scacchiera : "
        for p in self.pieces:
            s += str(p)+","
        return s

    def move_piece(self, pezzo, x_stat, y_stat):# pezzo
        try_pos = x_stat, y_stat
        possibili = pezzo.possible_poss()
        if try_pos in possibili:
            for p in self.pieces:  #  p è il pezzo attuale che ho in posizione...
                if type(p) == type(pezzo) and p.pos_in_x == pezzo.pos_in_x and p.pos_in_y == pezzo.pos_in_y:  #  try_pos è vedere se è possibile muoverlo la
                    self.pieces.remove(p)
                    pezzo.pos_in_x = x_stat
                    pezzo.pos_in_y = y_stat
                    self.pieces.append(pezzo)

        # self.pieces rimuove il pezzo e lo riaggiunge nella nuova posizione.



#devi implementare un metodo sulla scacchiera chiamato:

#sposta_pezzo(...)

#passando come parametri il pezzo che vuoi muovere e la nuova posizione.

#Questo metodo deve sparare un errore nel caso la nuova posizione non sia valida.