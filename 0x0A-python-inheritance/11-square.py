#!/usr/bin/python3
"""
Module for Square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a square"""


    def __init__(self, size):
        """Instantation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Print out parameters"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__, self.__size, self.__size)
