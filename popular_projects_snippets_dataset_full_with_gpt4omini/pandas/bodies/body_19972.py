# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
    If we have an axis, adapt the given key to be axis-independent.
    """
new_key = [slice(None)] * ndim
new_key[axis] = key
exit(tuple(new_key))
