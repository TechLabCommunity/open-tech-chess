from unittest import TestCase
from itertools import product
from king import King


class TestKing(TestCase):
    def test_possible_poss(self):
        xs = [chr(ord('a') + i) for i in range(0, 8)]
        ys = [i for i in range(1, 8)]
        for x, y in product(xs, ys):
            king = King(x, y)
            moves = list(product([ord(king.pos_in_x)], [y - 1, y + 1])) + list(product([ord(king.pos_in_x) - 1], [y - 1, y, y + 1])) \
                    + list(product([ord(king.pos_in_x) + 1], [y - 1, y, y + 1]))
            verifica = []
            for x, y in moves:
                if ord('a') <= x <= ord('h') and 1 <= y <= 8:
                    verifica.append((chr(x), y))

            try:
                self.assertTrue(sorted(verifica) == sorted(king.possible_poss()))
            except:
                print('Something is wrong')
                break
