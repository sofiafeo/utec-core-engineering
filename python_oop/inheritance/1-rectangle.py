#!/usr/bin/env python3
"""Define la clase Rectangle."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo."""

    def __init__(self, width, height):
        """Inicializa y valida el ancho y la altura."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
