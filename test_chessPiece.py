from itertools import product
from unittest import TestCase

from chess_piece import ChessPiece


class TestChessPiece(TestCase):
    def test_init(self):
        # test valido
        xs = [chr(ord('a')+p) for p in range(0, 8)] # a,b,c,d,e,f,g,h
        ys = [p for p in range(1, 9)] # 1,2,3,4,5,6,7,8
        for x,y in product(xs, ys):
            try:
                p = ChessPiece(x, y)
            except:
                self.fail(f'{x}{y} seems invalid...')
        xs = [chr(ord('i')+p) for p in range(0, 8)]
        ys = [i for i in range(9, 100)] + [i for i in range(-1, -30)]
        for x,y in product(xs, ys):
            try:
                p = ChessPiece(x, y)
                self.fail(f'{x}{y} seems valid but is not valid...')
            except:
                pass
