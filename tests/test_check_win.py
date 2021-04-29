import unittest
from src.check_win import*
from src.main import check_win


class TestCheckWin(unittest.TestCase):
    def test_check_diagonal(self):
        field = [["*"] * 3 for i in range(3)]
        self.assertEqual(check_diagonals(field, "X"), False)
        self.assertEqual(check_diagonals(field, "0"), False)

        field[0][0] = field[1][1] = field[2][2] = "X"
        self.assertEqual(check_diagonals(field, "X"), True)
        field[0][2] = field[1][1] = field[2][0] = "0"
        self.assertEqual(check_diagonals(field, "0"), True)

        field[0][2] = "X"
        self.assertEqual(check_diagonals(field, "X"), False)
        self.assertEqual(check_diagonals(field, "0"), False)


    def test_check_horizontals(self):
        field = [["*"] * 3 for i in range(3)]
        self.assertEqual(check_horizontals(field, "X"), False)
        self.assertEqual(check_horizontals(field, "0"), False)

        field[0][0] = field[0][1] = field[0][2] = "X"
        field[1][0] = field[1][1] = field[1][2] = "0"
        field[2][0] = field[2][1] = field[2][2] = "X"
        self.assertEqual(check_horizontals(field, "X"), True)
        self.assertEqual(check_horizontals(field, "0"), True)

        field[0][0] = field[2][0] = "0"
        field[1][1] = "X"
        self.assertEqual(check_horizontals(field, "X"), False)
        self.assertEqual(check_horizontals(field, "0"), False)


    def test_check_verticals(self):
        field = [["*"] * 3 for i in range(3)]
        self.assertEqual(check_verticals(field, "X"), False)
        self.assertEqual(check_verticals(field, "0"), False)

        field[0][0] = field[1][0] = field[2][0] = "X"
        field[0][1] = field[1][1] = field[2][1] = "0"
        field[0][2] = field[1][2] = field[2][2] = "X"
        self.assertEqual(check_verticals(field, "X"), True)
        self.assertEqual(check_verticals(field, "0"), True)

        field[0][0] = field[1][2] = "0"
        field[1][1] = "X"
        self.assertEqual(check_verticals(field, "X"), False)
        self.assertEqual(check_verticals(field, "0"), False)

    def test_check_win(self):
        field = [["*"] * 3 for i in range(3)]
        self.assertEqual(check_win(field, "X"), False)
        self.assertEqual(check_win(field, "0"), False)

        field[0][0] = field[0][1] = field[0][2] = "X"
        self.assertEqual(check_win(field, "X"), True)

        field[0][2] = field[1][2] = field[2][2] = "0"
        self.assertEqual(check_win(field, "0"), True)
        self.assertEqual(check_win(field, "X"), False)

        field[0][0] = field[1][1] = field[2][2] = "X"
        self.assertEqual(check_win(field, "X"), True)
        self.assertEqual(check_win(field, "0"), False)

        field[0][2] = field[1][1] = field[2][0] = "0"
        self.assertEqual(check_win(field, "0"), True)
        self.assertEqual(check_win(field, "X"), False)


