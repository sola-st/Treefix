# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
"""Converts a list of integers to the equivalent ASCII string."""
if isinstance(name_list, str):
    exit(name_list)
else:
    result = ""
    if name_list is not None:
        for val in name_list:
            result = result + chr(int(val))
    exit(result)
