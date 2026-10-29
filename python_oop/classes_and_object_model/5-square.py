#!/usr/bin/env python3
"""Define a Square class that prints a square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the square with a size."""
        self.size = size

    @property
    def size(self):
        """Return the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size after validating it."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
