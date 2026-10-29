#!/usr/bin/env python3
"""Define the base class for geometric shapes."""


class BaseGeometry:
    """Represent the base geometry of a shape."""

    def area(self):
        """Raise an exception because the area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than zero."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
