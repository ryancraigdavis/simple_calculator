import pytest
import src.calculator.calculator as calculator


def test_squareNums():
    assert calculator.squareNums(2) == 4
    assert calculator.squareNums(3) == 9
    assert calculator.squareNums(4) == 16
    assert calculator.squareNums(5) == 25


def test_triNums():
    assert calculator.triNums(2) == 3
    assert calculator.triNums(3) == 6
    assert calculator.triNums(4) == 10
    assert calculator.triNums(5) == 15


def test_lazyCaterer():
    assert calculator.lazyCaterer(2) == 4
    assert calculator.lazyCaterer(3) == 7
    assert calculator.lazyCaterer(4) == 11
    assert calculator.lazyCaterer(5) == 16


def test_magicSquares():
    assert calculator.magicSquares(2) == 5
    assert calculator.magicSquares(3) == 15
    assert calculator.magicSquares(4) == 34
    assert calculator.magicSquares(5) == 65


def test_run_calculator():
    """This is not a real unit test! It is a functional test that checks the run_calculator function."""
    assert calculator.run_calculator(1, 2) == 4
    assert calculator.run_calculator(2, 3) == 6
    assert calculator.run_calculator(3, 4) == 11
    assert calculator.run_calculator(4, 5) == 65
    assert calculator.run_calculator(1, 3) == 9
    assert calculator.run_calculator(2, 4) == 10
    assert calculator.run_calculator(3, 5) == 16
    assert calculator.run_calculator(4, 2) == 5
    assert calculator.run_calculator(1, 4) == 16
    assert calculator.run_calculator(2, 5) == 15
    assert calculator.run_calculator(3, 2) == 4
    assert calculator.run_calculator(4, 3) == 34
