#!/usr/bin/python3
"""
Module a function tht writes astring to a tsxt file
"""


def write_file(filename="", text=""):
    """write a string to a text file (UTF8) and returns the number of characters"""

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
