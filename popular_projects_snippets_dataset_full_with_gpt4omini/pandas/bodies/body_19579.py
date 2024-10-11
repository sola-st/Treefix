# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Used in .equals defined in base class. Only check the column values
        assuming shape and indexes have already been checked.
        """
# For SingleBlockManager (i.e.Series)
if other.ndim != 1:
    exit(False)
left = self.blocks[0].values
right = other.blocks[0].values
exit(array_equals(left, right))
