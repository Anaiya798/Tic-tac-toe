from src.check_win import*
from src.almost_win import*
from src.without_cross import*

def greeting():
    print("=================")
    print("RULES:")
    print("We are going to play tic-tac-toe! You play for crosses.")
    print("Each cell is specified by 2 coordinates in the range from 1 to 3.")
    print("For example, an input like '1 3' (without quotation marks!) means the 1st x and the 3rd yumn.")
    print("In your turn, you must enter the coordinates of the cell in which you want to put a cross.")
    print("ATTENTION: each coordinate must be entered on a new line!")
    print("Good luck!")
    print("=================")


def print_field(field):
    for x in range(3):
        print(*field[x])


def no_empty_cell(field):
    for row in range(3):
        for col in range(3):
            if field[row][col] == "*":
                return False
    return True


def check_win(field, symbol):
    if any([
        check_diagonals(field, symbol),
        check_horizontals(field, symbol),
        check_verticals(field, symbol)
    ]):
        return True
    return False


def almost_win(field, symbol):
    if almost_win_horizontal(field, symbol):
        return almost_win_horizontal(field, symbol)
    elif almost_win_vertical(field, symbol):
        return almost_win_vertical(field, symbol)
    elif almost_win_diagonal(field, symbol):
        return almost_win_diagonal(field, symbol)
    else:
        return False


def without_cross(field):
    if row_without_cross(field):
        return row_without_cross(field)
    elif col_without_cross(field):
        return col_without_cross(field)
    elif diagonal_without_cross(field):
        return diagonal_without_cross(field)
    else:
        return False


def first_zero_step(field):
    if field[1][1] == "*":
        field[1][1] = "0"
    else:
        field[0][0] = "0"


def put_zero(fun, *args):
    x = fun(*args)[0]
    y = fun(*args)[1]
    args[0][x][y] = "0"


def zero_strategy(field):
    if almost_win(field, "0"):
        put_zero(almost_win, field, "0")
    elif almost_win(field, "X"):
        put_zero(almost_win, field, "X")
    elif without_cross(field):
        put_zero(without_cross, field)
    else:
        for row in range(3):
            for col in range(3):
                if field[row][col] == "*":
                    field[row][col] = "0"
                    return


def game_cycle(field):
    step = 0
    while True:
        print_field(field)
        print("Put a cross: ")
        x, y = input(), input()

        if not(x.isdigit()) or not(y.isdigit()):
            print("Invalid input! Please, enter numbers")
            continue

        x = int(x)
        y = int(y)

        if any([x < 1, x > 3, y < 1, y > 3]):
            print("Invalid coordinates! Coordinates are in the range from 1 to 3")
            continue

        if field[x - 1][y - 1] != "*":
            print("This cell is not empty!")
            continue

        field[x - 1][y - 1] = "X"
        step = step + 1

        if check_win(field, "X"):
            print_field(field)
            print("You win! Congratulations!")
            break

        if no_empty_cell(field):
            print_field(field)
            print("Draw!")
            break

        if step == 1:
            first_zero_step(field)
        else:
            zero_strategy(field)

        if check_win(field, "0"):
            print_field(field)
            print("Unfortunately, you lose. Maybe, next time?")
            break

        if no_empty_cell(field):
            print_field(field)
            print("Draw!")
            break

            
if __name__ == '__main__':
   greeting()
   field = [["*"] * 3 for i in range(3)]
   game_cycle(field)