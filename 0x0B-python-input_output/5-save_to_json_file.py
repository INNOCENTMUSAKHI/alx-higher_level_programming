#!/usr/bin/python3
"""
A function that writes an object to text file 
using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an obj to txt file using a JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
