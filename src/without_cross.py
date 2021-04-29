
def row_without_cross(field):
    """Find a row without any cross"""
    for row in range(3):
       if any([
           field[row][0] == "X",
           field[row][1] == "X",
           field[row][2] == "X",
       ]):
           continue #skip if current row contains cross
       for col in range(3):
           if field[row][col] == "*": #empty cell in a row without cross found
               return(row, col)
    return False


def col_without_cross(field):
    """Find a column without any cross"""
    for col in range(3):
       if any([
            field[0][col] == "X",
            field[1][col] == "X",
            field[2][col] == "X",
       ]):
           continue #skip if current column contains cross
       for row in range(3):
           if field[row][col] == "*": #empty cell in a column without cross found
               return(row, col)
    return False


def diagonal_without_cross(field):
    """Find a column without any cross"""
    if all([
         field[0][0] != "X",
         field[1][1] != "X",
         field[2][2] != "X",
    ]): #check main diagonal doesn't contain crosses
       if field[0][0] == "*": #empty cell in  main diagonal without cross found
           return(0, 0)
       if field[1][1] == "*":
           return(1, 1)
       if field[2][2] == "*":
           return(2, 2)

    if all([
         field[0][2] != "X",
         field[1][1] != "X",
         field[2][0] != "X",
    ]): #check side diagonal doesn't contain crosses
       if field[0][2] == "*": #empty cell in  side diagonal without cross found
           return(0, 2)
       if field[1][1] == "*":
           return(1, 1)
       if field[2][0] == "*":
           return(2, 0)
    return False
