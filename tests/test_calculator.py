import pytest
from calculator.calculator import (
    squareNums,
    triNums,
    lazyCaterer,
    magicSquares,
    hypotenuse,
    factorial,
    celsius_to_fahrenheit,
)


@pytest.mark.parametrize("n, expected", [(2, 4), (5, 25), (0, 0)])
def test_squareNums(n, expected):
    assert squareNums(n) == expected


@pytest.mark.parametrize("n, expected", [(1, 1), (4, 10), (7, 28)])
def test_triNums(n, expected):
    assert triNums(n) == expected


@pytest.mark.parametrize("n, expected", [(1, 2), (3, 7), (5, 16)])
def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected


@pytest.mark.parametrize("n, expected", [(3, 15), (4, 34), (1, 1)])
def test_magicSquares(n, expected):
    assert magicSquares(n) == expected


@pytest.mark.parametrize("a, b, expected", [(3, 4, 5.0), (5, 12, 13.0), (8, 15, 17.0)])
def test_hypotenuse(a, b, expected):
    assert hypotenuse(a, b) == expected


@pytest.mark.parametrize("n, expected", [(0, 1), (5, 120), (7, 5040)])
def test_factorial(n, expected):
    assert factorial(n) == expected


@pytest.mark.parametrize("c, expected", [(0, 32), (100, 212), (-40, -40)])
def test_celsius_to_fahrenheit(c, expected):
    assert celsius_to_fahrenheit(c) == expected
