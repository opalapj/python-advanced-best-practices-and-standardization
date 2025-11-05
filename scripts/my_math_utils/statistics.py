"""
Statistical utilities.

This module provides basic statistical functions like mean, median, and variance.
"""

from typing import Iterable


def mean(data: Iterable[float]) -> float:
    """Compute the arithmetic mean.

    Args:
        data: A collection of numeric values.

    Returns:
        The mean of the data.

    Raises:
        ValueError: If `data` is empty.
    """
    data = list(data)
    if not data:
        raise ValueError("Data cannot be empty")
    return sum(data) / len(data)


def median(data: Iterable[float]) -> float:
    """Compute the median.

    Args:
        data: A collection of numeric values.

    Returns:
        The median value.
    """
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise ValueError("Data cannot be empty")
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]


def variance(data: Iterable[float]) -> float:
    """Compute the variance.

    Args:
        data: A collection of numeric values.

    Returns:
        The variance of the data.

    Raises:
        ValueError: If `data` contains fewer than two elements.
    """
    data = list(data)
    n = len(data)
    if n < 2:
        raise ValueError("At least two data points are required")
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (n - 1)
