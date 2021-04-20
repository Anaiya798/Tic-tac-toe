
def row_without_cross(field):
    for row in range(3):
       if any([
           field[row][0] == "X",
           field[row][1] == "X",
           field[row][2] == "X",
       ]):
           continue
       for col in range(3):
           if field[row][col] == "*":
               return(row, col)
    return False


def col_without_cross(field):
    for col in range(3):
       if any([
            field[0][col] == "X",
            field[1][col] == "X",
            field[2][col] == "X",
       ]):
           continue
       for row in range(3):
           if field[row][col] == "*":
               return(row, col)
    return False


def diagonal_without_cross(field):
    if all([
         field[0][0] != "X",
         field[1][1] != "X",
         field[2][2] != "X",
    ]):
       if field[0][0] == "*":
           return(0, 0)
       if field[1][1] == "*":
           return(1, 1)
       if field[2][2] == "*":
           return(2, 2)

    if all([
         field[0][2] != "X",
         field[1][1] != "X",
         field[2][0] != "X",
    ]):
       if field[0][2] == "*":
           return(0, 2)
       if field[1][1] == "*":
           return(1, 1)
       if field[2][0] == "*":
           return(2, 0)
    return False
