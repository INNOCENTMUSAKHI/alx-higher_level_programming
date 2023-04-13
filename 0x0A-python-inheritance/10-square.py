#!/usr/bin/python3
"""
Module 10-square.py
Calculate area of square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle, who inherits from BaseGeometry
    methods:
       __init__(self, size)
    """
    def __init__(self, size):
        """
        initializes size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
