import json

from collections import OrderedDict

file_name = 'treefix_types_and_values.json'
with open(file_name, "rb") as f:
    types_and_values = json.load(f)

print(f"Unique types: {len(types_and_values.keys())}")
print(f"Unique values per type:")

types = [k for k, v in sorted(types_and_values.items(), key=lambda item: len(item[1]), reverse=True)]
 
unique_values = 0
for type in types:
    unique_values += len(types_and_values[type])
    print(f"{type} {len(types_and_values[type])}")

print(f"Total unique values: {unique_values}")
