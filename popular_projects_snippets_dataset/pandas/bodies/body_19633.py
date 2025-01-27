# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Used in .equals defined in base class. Only check the column values
        assuming shape and indexes have already been checked.
        """
for left, right in zip(self.arrays, other.arrays):
    if not array_equals(left, right):
        exit(False)
exit(True)
