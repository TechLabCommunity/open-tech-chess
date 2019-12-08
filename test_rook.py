from unittest import TestCase
from itertools import product
from rook import Rook


class TestRook(TestCase):
    def test_possible_poss(self):
        xs = [chr(ord('a') + i) for i in range(0, 8)]
        ys = [i for i in range(1, 9)]
        for x, y in product(xs, ys):
            r = Rook(x, y)

            verifica= []
            for element_x in xs:
                if r.pos_in_x != element_x:
                    verifica.append((element_x, r.pos_in_y))
                elif r.pos_in_x == element_x:
                    for element_y in ys:
                        if element_y != r.pos_in_y:
                            verifica.append((r.pos_in_x, element_y))
            try:
                self.assertTrue(sorted(verifica) == sorted(r.possible_poss()))
            except:
                print('Something is wrong')
                break

