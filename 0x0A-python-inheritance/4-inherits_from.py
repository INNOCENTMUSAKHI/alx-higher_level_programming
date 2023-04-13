#!/usr/bin/python3
"""
Module 4-inherits_from.py

Contains method inherits_from
return True is obj us instance of class that it inherits from or is subcls of
"""


def inherits_from(obj, a_class):
    """returns True if object is an instance of a class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
