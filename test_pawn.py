from itertools import product
from unittest import TestCase
from pawn import Pawn


class TestPawn(TestCase):
    def test_init(self):
        # test valido
        xs = [chr(ord('a')+i) for i in range(0, 8)]
        ys = [i for i in range(1, 8)]
        for x, y in product(xs, ys):
            p = Pawn(x, y)
            try:
                self.assertTrue([(x, y+1)] == p.possible_poss())
            except:
                print(f'{x},{y} should be valid with {x}{y+1}')
