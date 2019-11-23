from pawn import Pawn
from knight import Knight
from rook import Rook
from king import King
from bishop import Bishop
from queen import Queen
from chess import Chess

#ped_1 = Pawn(input("metti posizione x: "), int(input("metti posizione y: ")))
#ped_1.pos_pawn()


#cav_1 = Knight(input("metti posizione x: "), int(input("metti posizione y: ")))
#cav_1.pos_knight()

#king_1 = King(input("metti posizione x: "), int(input("metti posizione y: ")))
#king_1.pos_king()


#tor_1 = Rook(input("metti posizione x: "), int(input("metti posizione y: ")))
#tor_1.pos_rook()

#alfiere_1 = Bishop(input("metti posizione x: "), int(input("metti posizione y: ")))
#alfiere_1.pos_bishop()

# input_x = input("metti posizione x: ")
# input_y = int(input("metti posizione y: "))
regina_1 = Queen('a', 3)
regina_2 = Queen('h', 8)
alfiere = Bishop('g', 7)
pedone = Pawn('g', 7)
# questo è comodo. Può stampare a video perchè ha ereditato da ChessPiece __str__
#regina_1.pos_queen()

c = Chess()
c.set_piece(regina_1)
c.set_piece(regina_2)
c.set_piece(alfiere)
c.set_piece(pedone)  # alfiere sparisce perchè pedone prende il suo posto.
print(c)
c.move_piece(regina_1, x_stat="a", y_stat=6)
print(c)
# ricordati di fare gli unittest magari sulle classi...

#devi implementare un metodo sulla scacchiera chiamato:

#sposta_pezzo(...)

#passando come parametri il pezzo che vuoi muovere e la nuova posizione.

#Questo metodo deve sparare un errore nel caso la nuova posizione non sia valida.