#!/usr/bin/python3
"""
This module defines a Square class with validation for size.
"""


class Square:
    """
    Represents a square with private instance attribute size.
    """

    def __init__(self, size=0):
        """
        Initializes the square and validates the size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
