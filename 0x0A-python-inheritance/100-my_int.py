#!/usr/bin/python3
"""
Module class MyInt that inherits from int
"""


class MyInt(int):
    """initializing class"""
    def __eq__(self, other):
        """
        Return:
            True if both not equal
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """
        Return:
            True if both equal
        """
        return int(self) == int(other)
