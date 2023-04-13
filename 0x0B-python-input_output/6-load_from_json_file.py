#!/usr/bin/python3
"""
A function that create an obj
from a JSON file
"""


import json


def load_from_json_file(filename):
    """create obj from JSON file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
