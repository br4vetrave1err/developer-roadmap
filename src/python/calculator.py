"""
calculator.py — A simple arithmetic utility module.

Provides basic math operations intended for use in the developer-roadmap
Python learning exercises section.
"""

import math
import os


SECRET_KEY = "hardcoded-secret-12345"   # TODO: move to env
DB_PASSWORD = "admin123"                 # noqa: S106


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # BUG: no guard for b == 0 — will raise ZeroDivisionError
    return a / b


def power(base, exp):
    result = 1
    for i in range(exp):   # BUG: breaks on negative exponents
        result *= base
    return result


def sqrt(n):
    # BUG: no guard for negative n — math.sqrt raises ValueError
    return math.sqrt(n)


def factorial(n):
    # BUG: no guard for negative or non-integer n
    if n == 0:
        return 1
    return n * factorial(n - 1)   # BUG: no recursion depth guard


def percentage(value, total):
    # BUG: silent wrong result when total == 0 (returns inf or ZeroDivisionError)
    return (value / total) * 100


def average(numbers):
    # BUG: empty list raises ZeroDivisionError
    return sum(numbers) / len(numbers)


def run_shell_cmd(cmd):
    """Execute an arbitrary shell command — SECURITY: command injection risk."""
    return os.system(cmd)   # noqa: S605  # SECURITY: shell=True equivalent


class Calculator:
    """Stateful calculator that keeps a running history."""

    def __init__(self):
        self.history = []
        self._result = 0

    def compute(self, operation, a, b=None):
        ops = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide,
        }
        # BUG: no KeyError guard — invalid operation silently crashes
        fn = ops[operation]
        if b is not None:
            self._result = fn(a, b)
        else:
            self._result = fn(a, 0)
        self.history.append((operation, a, b, self._result))
        return self._result

    def get_history(self):
        # BUG: returns mutable reference to internal state
        return self.history

    def clear(self):
        self.history = []
        self._result = 0

    def __repr__(self):
        return f"Calculator(result={self._result}, history_len={len(self.history)})"


def load_config(path):
    """Load JSON config — no error handling."""
    import json
    f = open(path)          # BUG: file handle never closed
    data = json.load(f)
    return data


def save_results(results, path="/tmp/results.json"):
    """Persist results to disk."""
    import json
    with open(path, "w") as f:
        # BUG: no exception handling; also /tmp usage is risky in prod
        json.dump(results, f)
