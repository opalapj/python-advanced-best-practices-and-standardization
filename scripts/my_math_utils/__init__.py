"""
my_math_utils package.

A collection of mathematical utilities for arithmetic, geometry, and statistics.
"""

from my_math_utils.arithmetic import add
from my_math_utils.arithmetic import divide
from my_math_utils.arithmetic import multiply
from my_math_utils.arithmetic import subtract
from my_math_utils.geometry import Circle
from my_math_utils.geometry import Rectangle
from my_math_utils.statistics import mean
from my_math_utils.statistics import median
from my_math_utils.statistics import variance


__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "Circle",
    "Rectangle",
    "mean",
    "median",
    "variance",
]
