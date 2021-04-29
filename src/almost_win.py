
def almost_win_horizontal(field, symbol):
  """Check any horizontal is almost filled with zeros/crosses"""
  for row in range(3):
        for col in range(2):
            if col == 0:
                if field[row][col] == field[row][col + 1] == symbol and field[row][col + 2] == "*": #1,2 column filled
                    return(row, col + 2)
                if field[row][col] == field[row][col + 2] == symbol and field[row][col + 1] == "*": #1,3 column filled
                    return(row, col + 1)
            if col == 1:
                if field[row][col] == field[row][col + 1] == symbol and field[row][col - 1] == "*": #2,3 column filled
                     return(row, col - 1)
  return False


def almost_win_vertical(field, symbol):
  """Check any vertical is almost filled with zeros/crosses"""
  for row in range(2):
        for col in range(3):
            if row == 0:
                if field[row][col] == field[row + 1][col] == symbol and field[row + 2][col] == "*": #1,2 row filled
                    return(row + 2, col)
                if field[row][col] == field[row + 2][col] == symbol and field[row + 1][col] == "*": #1,3 row filled
                    return(row + 1, col)
            if row == 1:
                if field[row][col] == field[row + 1][col] == symbol and field[row - 1][col] == "*": #2,3 column filled
                    return(row - 1, col)
  return False


def almost_win_diagonal(field, symbol):
  """Check any diagonal is almost filled with zeros/crosses"""
  if field[0][0] == field[1][1] == symbol and field[2][2] == "*": #1,2 cells in main filled
       return(2, 2)
  if field[0][0] == field[2][2] == symbol and field[1][1] == "*": #1,3 cells in main filled
       return(1, 1)
  if field[1][1] == field[2][2] == symbol and field[0][0] == "*": #2,3 cells in main filled
       return(0, 0)

  if field[0][2] == field[1][1] == symbol and field[2][0] == "*": #1,2 cells in side filled
      return(2, 0)
  if field[0][2] == field[2][0] == symbol and field[1][1] == "*": #1,3 cells in side filled
      return(1, 1)
  if field[1][1] == field[2][0] == symbol and field[0][2] == "*": #2,3 cells in side filled
      return(0, 2)
  return False
