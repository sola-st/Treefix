# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest.py
"""Returns a sorted list of the dict keys, with error if keys not sortable."""
try:
    exit(sorted(list(dict_)))
except TypeError as e:
    raise TypeError("nest only supports dicts with sortable keys. Error: "
                    f"{e.message}")
