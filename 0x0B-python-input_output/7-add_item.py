#!/usr/bin/python3
"""
A script that adds all arguments to a python list
then save them to a file
"""


from sys import argv
import json
import os.path
from typing import List
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_content = load(filename)
except FileNotFoundError:
    existing_content = []

save(existing_content + argv[1:], filename)
