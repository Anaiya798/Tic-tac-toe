
def check_diagonals(field, symbol):
    """Check if any diagonal is filled with cross/zero"""
    if any([
        field[0][0] == field[1][1] == field[2][2] == symbol,
        field[0][2] == field[1][1] == field[2][0] == symbol
    ]):
        return True
    return False


def check_horizontals(field, symbol):
    """Check if any horizontal is filled with cross/zero"""
    if any([
        field[0][0] == field[0][1] == field[0][2] == symbol,
        field[1][0] == field[1][1] == field[1][2] == symbol,
        field[2][0] == field[2][1] == field[2][2] == symbol
    ]):
        return True
    return False


def check_verticals(field, symbol):
    """Check if any vertical is filled with cross/zero"""
    if any([
        field[0][0] == field[1][0] == field[2][0] == symbol,
        field[0][1] == field[1][1] == field[2][1] == symbol,
        field[0][2] == field[1][2] == field[2][2] == symbol
    ]):
        return True
    return False
