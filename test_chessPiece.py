from unittest import TestCase

from chess_piece import ChessPiece


class TestChessPiece(TestCase):
    def test_init(self):
        # test valido
        try:
            p = ChessPiece('a', 6)
        except ValueError:
            self.fail(f'piece has to be valid.')

        # test lettera sbagliata, deve lanciare un errore.
        try:
            p = ChessPiece('r', 4)
            self.fail()
        except:
            # all right bitches, r is invalid.
            pass

        # test numero sbagliato, deve lanciare un errore.
        try:
            p = ChessPiece('h', 10)
            self.fail()
        except:
            # all right bitches, 10 is invalid.
            pass
