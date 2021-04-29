from src.check_win import*
from src.almost_win import*
from src.without_cross import*

def greeting():
    """Greetings and game rules"""
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
    """Print current state of game field"""
    for x in range(3):
        print(*field[x])


def no_empty_cell(field):
    """Is it draw?"""
    for row in range(3): #if no empty cells found, it considered to be draw
        for col in range(3):
            if field[row][col] == "*":
                return False
    return True


def check_win(field, symbol):
    """Does user/computer win?"""
    if any([
        check_diagonals(field, symbol),
        check_horizontals(field, symbol),
        check_verticals(field, symbol)
    ]):
        return True
    return False


def almost_win(field, symbol):
    """Is user/computer going to win?"""
    if almost_win_horizontal(field, symbol): #almost win horizontally
        return almost_win_horizontal(field, symbol)
    elif almost_win_vertical(field, symbol): #almost win vertically
        return almost_win_vertical(field, symbol)
    elif almost_win_diagonal(field, symbol): #almost win diagonally
        return almost_win_diagonal(field, symbol)
    else:
        return False


def without_cross(field):
    """Finding a line without cross"""
    if row_without_cross(field): #row
        return row_without_cross(field)
    elif col_without_cross(field): #column
        return col_without_cross(field)
    elif diagonal_without_cross(field): #diagonal
        return diagonal_without_cross(field)
    else: #no lines
        return False


def first_zero_step(field):
    """Zero first step strategy"""
    if field[1][1] == "*":
        field[1][1] = "0"
    else:
        field[0][0] = "0"


def put_zero(fun, *args):
    """Put zero in a cell with certain coordinates"""
    x = fun(*args)[0]
    y = fun(*args)[1]
    args[0][x][y] = "0"


def zero_strategy(field):
    """Optimal computer strategy"""
    if almost_win(field, "0"): #computer's going to win
        put_zero(almost_win, field, "0")
    elif almost_win(field, "X"): #user's going to win
        put_zero(almost_win, field, "X")
    elif without_cross(field): #check line without cross
        put_zero(without_cross, field)
    else: #check any empty cell
        for row in range(3):
            for col in range(3):
                if field[row][col] == "*":
                    field[row][col] = "0"
                    return


def game_cycle(field):
    """Doing game cycle"""
    step = 0
    while True:
        print_field(field) #current state of game field
        print("Put a cross: ")
        x, y = input(), input() #user input

        if not(x.isdigit()) or not(y.isdigit()): #not numbers
            print("Invalid input! Please, enter numbers")
            continue

        x = int(x) #convertion to int format
        y = int(y)

        if any([x < 1, x > 3, y < 1, y > 3]): #out of range
            print("Invalid coordinates! Coordinates are in the range from 1 to 3")
            continue

        if field[x - 1][y - 1] != "*":  #cell is not empty
            print("This cell is not empty!")
            continue

        field[x - 1][y - 1] = "X" #put a cross
        step = step + 1 #increase step counter

        if check_win(field, "X"): #if user win
            print_field(field)
            print("You win! Congratulations!")
            break

        if no_empty_cell(field): #draw after users move
            print_field(field)
            print("Draw!")
            break

        if step == 1: #put a zero
            first_zero_step(field)
        else:
            zero_strategy(field)

        if check_win(field, "0"): #computer win
            print_field(field)
            print("Unfortunately, you lose. Maybe, next time?")
            break

        if no_empty_cell(field): #draw after computers move
            print_field(field)
            print("Draw!")
            break

            
if __name__ == '__main__':
   """Let's begin tic-tac-toe!"""
   greeting() #print greeting message
   field = [["*"] * 3 for i in range(3)] #create game field
   game_cycle(field) #enter game cecle