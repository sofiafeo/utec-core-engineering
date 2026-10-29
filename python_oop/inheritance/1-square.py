#!/usr/bin/env python3
"""Define la clase Square."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado."""

    def __init__(self, size):
        """Inicializa y valida el tamaño del cuadrado."""
        BaseGeometry = __import__('base_geometry').BaseGeometry
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calcula el área del cuadrado."""
        return self.__size * self.__size
