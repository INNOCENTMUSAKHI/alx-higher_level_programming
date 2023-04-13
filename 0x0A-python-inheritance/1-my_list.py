#!/usr/bin/python3
"""
Module 1-my_list.py
Prints a list in sorted form
"""


class MyList(list):
    """
    inherits from list

    methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """prints list of ints in ascending order"""
        print(sorted(self))
