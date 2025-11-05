"""
Geometric shapes and calculations.

This module defines common geometric shapes and methods to calculate
their properties such as area and perimeter.
"""

import math


class Circle:
    """Represents a circle."""

    def __init__(self, radius: float):
        """Initialize a Circle instance.

        Args:
            radius: The radius of the circle.

        Raises:
            ValueError: If the radius is not positive.
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle.

        Returns:
            The area of the circle.
        """
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        """Calculate the circumference (perimeter) of the circle.

        Returns:
            The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width: float, height: float):
        """Initialize a Rectangle instance.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.

        Raises:
            ValueError: If width or height is not positive.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)
