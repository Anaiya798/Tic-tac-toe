import unittest
from src.without_cross import*
from src.main import without_cross

class TestWithoutCross(unittest.TestCase):
   def test_row_without_cross(self):
       field = [["*"] * 3 for i in range(3)]
       self.assertEqual(row_without_cross(field), (0, 0))

       field[0][0] = field[1][2] = "X"
       field[2][0] = "0"
       self.assertEqual(row_without_cross(field), (2, 1))

       field[2][0] = "X"
       self.assertEqual(row_without_cross(field), False)

   def test_col_without_cross(self):
       field = [["*"] * 3 for i in range(3)]
       self.assertEqual(col_without_cross(field), (0, 0))

       field[1][0] = field[2][2] = "X"
       field[0][1] = field[1][1] = "0"
       self.assertEqual(col_without_cross(field), (2, 1))

       field[2][1] = "X"
       self.assertEqual(col_without_cross(field), False)

   def test_diagonal_without_cross(self):
       field = [["*"] * 3 for i in range(3)]
       self.assertEqual(diagonal_without_cross(field), (0, 0))

       field[0][0] = "0"
       self.assertEqual(diagonal_without_cross(field), (1, 1))

       field[2][2] = "X"
       field[0][2] = field[1][1] = "0"
       self.assertEqual(diagonal_without_cross(field), (2, 0))

       field[1][1] = "X"
       self.assertEqual(diagonal_without_cross(field), False)

   def test_without_cross(self):
       field = [["*"] * 3 for i in range(3)]
       self.assertEqual(without_cross(field), (0, 0))

       field[0][0] = field[2][2] = "X"
       field[1][0] = "0"
       self.assertEqual(without_cross(field), (1, 1))

       field[0][2] = field[1][2] = "X"
       field[0][0] = "0"
       self.assertEqual(without_cross(field), (2, 0))

       field[2][0] = field[0][1] = "X"
       field[2][2] = "*"
       self.assertEqual(without_cross(field), (1, 1))

       field[0][2] = field[2][0] = "*"
       field[2][2] = field[1][0] = "X"
       self.assertEqual(without_cross(field), (0, 2))

       field[1][1] = "X"
       self.assertEqual(without_cross(field), False)
