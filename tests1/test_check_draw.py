import unittest
from src.main import no_empty_cell

class TestDraw(unittest.TestCase):
    def test_no_empty_cell(self):
        field = [["*"] * 3 for i in range(3)]
        self.assertEqual(no_empty_cell(field), False)

        for row in range(3):
            for col in range(3):
                if abs(row - col) == 1:
                    field[row][col] = "X"
                else:
                    field[row][col] = "0"
        self.assertEqual(no_empty_cell(field), True)

        field[0][0] = "*"
        self.assertEqual(no_empty_cell(field), False)