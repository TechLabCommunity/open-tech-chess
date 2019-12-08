from unittest import TestCase
from itertools import product
from queen import Queen


class TestQueen(TestCase):
    def test_init(self):
        # test valido
        xs = [chr(ord('a')+i) for i in range(0, 8)]
        ys = [i for i in range(1, 9)]

        for x, y in product(xs, ys):
            q = Queen(x, y)

            verifica = []
            for element_x in xs:
                if q.pos_in_x != element_x:
                    verifica.append((element_x, q.pos_in_y))
                elif q.pos_in_x == element_x:
                    for element_y in ys:
                        if element_y != q.pos_in_y:
                            verifica.append((q.pos_in_x, element_y))

            try:
                self.assertTrue(sorted(verifica) == sorted(q.possible_poss()))
            except:
                print('Something is wrong')
                break
