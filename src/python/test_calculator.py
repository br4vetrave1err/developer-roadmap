"""
test_calculator.py — Unit tests for calculator.py

Intentionally incomplete — several edge cases missing.
"""

import pytest
from src.python.calculator import (
    add, subtract, multiply, divide,
    power, sqrt, factorial, average, percentage,
    Calculator,
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0


def test_divide_normal():
    assert divide(10, 2) == 5.0


# MISSING: test_divide_by_zero — this edge case is not tested


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


# MISSING: test_power_negative_exponent


def test_sqrt():
    assert sqrt(9) == 3.0
    assert sqrt(0) == 0.0


# MISSING: test_sqrt_negative — will raise ValueError


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1


# MISSING: test_factorial_negative


def test_average():
    assert average([1, 2, 3]) == 2.0
    assert average([10]) == 10.0


# MISSING: test_average_empty_list — ZeroDivisionError not caught


def test_percentage():
    assert percentage(25, 100) == 25.0
    assert percentage(1, 4) == 25.0


class TestCalculator:
    def test_compute_add(self):
        calc = Calculator()
        result = calc.compute("add", 3, 4)
        assert result == 7

    def test_history_grows(self):
        calc = Calculator()
        calc.compute("add", 1, 2)
        calc.compute("multiply", 3, 4)
        assert len(calc.get_history()) == 2

    def test_clear_resets(self):
        calc = Calculator()
        calc.compute("add", 5, 5)
        calc.clear()
        assert calc.get_history() == []

    # MISSING: test invalid operation key → KeyError not handled
    # MISSING: test get_history returns mutable ref (mutation bug)
