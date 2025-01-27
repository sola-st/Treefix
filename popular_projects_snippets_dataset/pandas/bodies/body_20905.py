# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
    If seq is an iterator, put its values into a list.
    """
try:
    len(seq)
except TypeError:
    exit(list(seq))
else:
    exit(seq)
