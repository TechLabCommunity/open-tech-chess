from unittest import TestCase
from itertools import product
from bishop import Bishop


class TestBishop(TestCase):
    def test_init(self):
        xs = [chr(ord('a') + i) for i in range(0, 8)]
        ys = [i for i in range(1, 9)]

        for x, y in product(xs, ys):
            b = Bishop(x, y)
            verifica = []
            count = 0
            for n in range(1, 9):
                if n <= 8:
                    count += 1
                    moves = list(product([ord(b.pos_in_x) + count], [b.pos_in_y + count]))
                    for x_m, y_m in moves:
                        if ord('a') <= x_m <= ord('h') and 1 <= y_m <= 8:
                            verifica.append((chr(x_m), y_m))
                    moves.clear()
            count = 0
            for n in range(1, 9):
                if n <= 8:
                    count += 1
                    moves_1 = list(product([ord(b.pos_in_x) - count], [b.pos_in_y + count]))
                    for x_m, y_m in moves_1:
                        if ord('a') <= x_m <= ord('h') and 1 <= y_m <= 8:
                            verifica.append((chr(x_m), y_m))
                    moves_1.clear()

            count = 0
            for n in range(1, 9):
                count += 1
                moves_2 = list(product([ord(b.pos_in_x) - count], [b.pos_in_y - count]))
                for x_m, y_m in moves_2:
                    if ord('a') <= x_m <= ord('h') and 1 <= y_m <= 8:
                        verifica.append((chr(x_m), y_m))
                moves_2.clear()

            count = 0
            for n in range(1, 9):
                count += 1
                moves_3 = list(product([ord(b.pos_in_x) + count], [b.pos_in_y - count]))
                for x_m, y_m in moves_3:
                    if ord('a') <= x_m <= ord('h') and 1 <= y_m <= 8:
                        verifica.append((chr(x_m), y_m))
                moves_3.clear()

            try:
                self.assertTrue(sorted(verifica) == sorted(b.possible_poss()))


            except:
                print('Something is wrong')
                break
