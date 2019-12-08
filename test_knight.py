from itertools import product
from unittest import TestCase
from knight import Knight


class TestKnight(TestCase):
    def test_init(self):
        # test valido
        xs = [chr(ord('a') + i) for i in range(0, 8)]
        ys = [i for i in range(1, 8)]
        for x, y in product(xs, ys):
                k = Knight(x, y)
                moves = list(product([ord(x) - 1, ord(x) + 1], [y - 2, y + 2])) + list(product([ord(x) - 2, ord(x) + 2], [y - 1, y + 1]))
                result_moves = []
                for x, y in moves:
                    if ord('a') <= x <= ord('h') and 1 <= y <= 8:
                        result_moves.append((chr(x), y))

                try:
                    self.assertTrue(sorted(result_moves) == sorted(k.possible_poss()))
                except:
                    print(f'Somethings wrong...')


