import sys


def squareNums(n):
    """Calculates the square"""
    return n ** 2


def triNums(n):
    """Calculates the tri number"""
    return (n * (n + 1)) / 2


def lazyCaterer(n):
    """Calculates the lazy caterer number"""
    return (n ** 2 + n + 2) / 2


def magicSquares(n):
    """Calculates the magic squares number"""
    return (n * (n ** 2 + 1)) / 2


if __name__ == "__main__":
    calculator = {
        "square": squareNums,
        "tri": triNums,
        "lazy_caterer": lazyCaterer,
        "magic_squares": magicSquares,
    }
    input_formula = calculator[sys.argv[1]]
    result = input_formula(int(sys.argv[2]))
    print(result)
