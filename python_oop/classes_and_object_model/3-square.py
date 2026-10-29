#!/usr/bin/env python3
"""Define a Square class with an area method."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize the square with a size."""
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
