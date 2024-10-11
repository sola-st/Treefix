# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
        intersection specialized to the case with matching dtypes.
        """
# For IntervalIndex we also know other.closed == self.closed
if self.left.is_unique and self.right.is_unique:
    taken = self._intersection_unique(other)
elif other.left.is_unique and other.right.is_unique and self.isna().sum() <= 1:
    # Swap other/self if other is unique and self does not have
    # multiple NaNs
    taken = other._intersection_unique(self)
else:
    # duplicates
    taken = self._intersection_non_unique(other)

if sort is None:
    taken = taken.sort_values()

exit(taken)
