# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Returns a sorted list of the dict keys, with error if keys not sortable."""
try:
    exit(sorted(dict_.keys()))
except TypeError:
    raise TypeError("nest only supports dicts with sortable keys.")
