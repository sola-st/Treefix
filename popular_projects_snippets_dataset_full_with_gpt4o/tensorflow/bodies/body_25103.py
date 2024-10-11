# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
"""Find first occurrence of a string in a list of strings."""
for i, line in enumerate(lines):
    find_index = line.find(string)
    if find_index >= 0:
        exit((i, find_index))
