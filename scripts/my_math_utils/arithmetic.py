"""
Basic arithmetic operations.

This module provides simple arithmetic functions such as addition, subtraction,
multiplication, and division.
"""


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of `a` and `b`.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract one number from another.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The result of `a - b`.

    Raises:
        TypeError: If either argument is not a number.
    """
    if not all(isinstance(x, (int, float)) for x in (a, b)):
        raise TypeError("Both arguments must be numbers")
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of `a` and `b`.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide one number by another.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The result of `a / b`.

    Raises:
        ZeroDivisionError: If `b` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
