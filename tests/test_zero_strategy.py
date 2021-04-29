import unittest
from src.main import zero_strategy


class TestZeroStrategy(unittest.TestCase):
    def test_zero_strategy(self):
        field = [["*"] * 3 for i in range(3)]
        field[0][0] = field[0][1] = field[2][2] = "X"
        field[2][0] = field[2][1] = "0"
        should_be = field
        should_be[0][2] = "0"
        zero_strategy(field)
        self.assertEqual(field, should_be)

        field[1][2] = "X"
        should_be[1][1] = "0"
        zero_strategy(field)
        self.assertEqual(field, should_be)

        field = [["*"] * 3 for i in range(3)]
        field[0][0] = field[2][2] = "X"
        field[1][1] = "0"
        should_be = field
        should_be[0][1] = "0"
        zero_strategy(field)
        self.assertEqual(field, should_be)

        field = [["*"] * 3 for i in range(3)]
        field[0][0] = field[1][0] = field[2][1] = "X"
        field[2][0] = "0"
        should_be = field
        should_be[0][2] = "0"
        zero_strategy(field)
        self.assertEqual(field, should_be)

        field = [["*"] * 3 for i in range(3)]
        field[0][0] = field[1][2] = field[2][1] = "X"
        should_be = field
        should_be[0][2] = "0"
        zero_strategy(field)
        self.assertEqual(field, should_be)

        field[0][0] = field[0][1] = field[1][2] = field[2][0] = field[2][2] = "X"
        field[0][2] = field[1][0] = field[1][1] = "0"
        should_be = field
        should_be[2][1] = "0"
        zero_strategy(field)
        self.assertEqual(field, should_be)


