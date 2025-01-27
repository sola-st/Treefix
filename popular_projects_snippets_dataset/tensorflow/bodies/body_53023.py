# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/utils.py
"""Returns a tuple with given shape and filled with value."""
if shape:
    exit(tuple([_create_tuple(shape[1:], value) for _ in range(shape[0])]))
exit(value)
