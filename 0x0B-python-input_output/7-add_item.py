#!/usr/bin/python3

import json
import sys
import os.path

def save_to_json_file(obj, filename):
    with open(filename, 'w') as f:
        json.dump(obj, f)

def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

filename = "add_item.json"
if os.path.isfile(filename):
    obj = load_from_json_file(filename)
else:
    obj = []

try:
    # Validate input as JSON
    for arg in sys.argv[1:]:
        obj.append(json.loads(arg))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

save_to_json_file(obj, filename)
