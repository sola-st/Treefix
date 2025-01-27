# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/common.py
"""
    For tests using tables, try removing the table to be sure there is
    no content from previous tests using the same table name.
    """
try:
    store.remove(key)
except (ValueError, KeyError):
    pass
