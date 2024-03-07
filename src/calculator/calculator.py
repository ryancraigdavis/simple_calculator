"""This module contains the calculator functions for the formulas square, tri, lazy caterer, and magic squares"""

import random


def squareNums(n):
    """Calculates the square"""
    return n**2


def multiplyRandNum(n):
    rand_num = random.randrange(1, 100)
    print(f"{n} multiplied by {rand_num}")
    return n * rand_num


def triNums(n):
    """Calculates the tri number"""
    return (n * (n + 1)) / 2


def lazyCaterer(n):
    """Calculates the lazy caterer number"""
    return (n**2 + n + 2) / 2


def magicSquares(n):
    """Calculates the magic squares number"""
    return (n * (n**2 + 1)) / 2


def run_calculator(input_formula, input_num):
    """Calls and returns results for the specified formulas"""
    calculator = [squareNums, triNums, lazyCaterer, magicSquares, multiplyRandNum]
    formula = calculator[input_formula - 1]
    return_result = formula(input_num)
    return return_result


if __name__ == "__main__":
    print(
        "Choose which formula to use: 1 for square, 2 for tri, 3 for lazy caterer, 4 for magic squares"
    )
    input_formula = int(input())
    print(
        "Enter a number to calculate the square, tri, lazy caterer, and magic squares numbers"
    )
    input_num = int(input())

    result = run_calculator(input_formula, input_num)
    print(result)
