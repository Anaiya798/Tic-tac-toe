import unittest
from src.almost_win import*
from src.main import almost_win


class TestAlmostWin(unittest.TestCase):
    def test_almost_win_horizontal(self):
        field = [["*"] * 3 for i in range(3)]
        self.assertEqual(almost_win_horizontal(field, "X"), False)
        self.assertEqual(almost_win_horizontal(field, "0"), False)

        field[0][0] = field[0][1] = "X"
        field[1][0] = field[1][2] = "0"
        self.assertEqual(almost_win_horizontal(field, "X"), (0, 2))
        self.assertEqual(almost_win_horizontal(field, "0"), (1, 1))

        field[0][0] = field[2][0] = field[2][2] = "0"
        field[0][2] = field[1][1] = "X"
        self.assertEqual(almost_win_horizontal(field, "X"), False)
        self.assertEqual(almost_win_horizontal(field, "0"), (2, 1))

    def test_almost_win_vertical(self):
        field = [["*"] * 3 for i in range(3)]
        self.assertEqual(almost_win_vertical(field, "X"), False)
        self.assertEqual(almost_win_vertical(field, "0"), False)

        field[0][0] = field[1][0] = "X"
        field[1][1] = field[2][1] = "0"
        self.assertEqual(almost_win_vertical(field, "X"), (2, 0))
        self.assertEqual(almost_win_vertical(field, "0"), (0, 1))

        field[0][1] = field[0][2] = field[2][2] = "X"
        field[2][0] = "0"
        self.assertEqual(almost_win_vertical(field, "X"), (1, 2))
        self.assertEqual(almost_win_vertical(field, "0"), False)

    def test_almost_win_diagonal(self):
        field = [["*"] * 3 for i in range(3)]
        self.assertEqual(almost_win_diagonal(field, "X"), False)
        self.assertEqual(almost_win_diagonal(field, "0"), False)

        field[0][0] = field[2][2] = "X"
        field[0][2] = field[2][0] = "0"
        self.assertEqual(almost_win_diagonal(field, "X"), (1, 1))
        self.assertEqual(almost_win_diagonal(field, "0"), (1, 1))

        field[1][1] = "0"
        field[0][2] = "*"
        self.assertEqual(almost_win_diagonal(field, "X"), False)
        self.assertEqual(almost_win_diagonal(field, "0"), (0, 2))

    def test_almost_win(self):
        field = [["*"] * 3 for i in range(3)]
        self.assertEqual(almost_win(field, "X"), False)
        self.assertEqual(almost_win(field, "0"), False)

        field[0][0] = field[0][1] = "X"
        self.assertEqual(almost_win(field, "X"), (0, 2))

        field[0][1] = field[1][1] = "0"
        self.assertEqual(almost_win(field, "X"), False)
        self.assertEqual(almost_win(field, "0"), (2, 1))

        field[1][1] = field[2][2] = "X"
        field[0][0] = "*"
        self.assertEqual(almost_win(field, "X"), (0, 0))
        self.assertEqual(almost_win(field, "0"), False)

        field[1][1] = field[0][2] = "0"
        field[0][1] = "X"
        self.assertEqual(almost_win(field, "X"), False)
        self.assertEqual(almost_win(field, "0"), (2, 0))

