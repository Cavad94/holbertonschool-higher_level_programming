#!/usr/bin/python3
"""
This module defines a Square class that can calculate its area.
"""


class Square:
    """
    Represents a square with private size and area calculation.
    """

    def __init__(self, size=0):
        """
        Initializes the square.
        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.
        Returns:
            The area (size squared).
        """
        return self.__size ** 2
