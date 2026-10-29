#!/usr/bin/env python3
"""Define a Square class with position and string representation."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the square position."""
        return self.__position


    @position.setter
    def position(self, value):
        """Set the square position after validating it."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(
                isinstance(coordinate, int)
                and not isinstance(coordinate, bool)
                and coordinate >= 0
                for coordinate in value
            )
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

            raise TypeError(
                "position must be a tuple of 2 positive integer"
            )
        self.__position = value

    def area(self):
        """Return the square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(
                " " * self.__position[0] + "#" * self.__size
            )

    def __str__(self):
        """Return the square representation."""
        if self.__size == 0:
            return ""
        rows = [" " * self.__position[0] + "#" * self.__size
                for _ in range(self.__size)]
        return "\n" * self.__position[1] + "\n".join(rows)
