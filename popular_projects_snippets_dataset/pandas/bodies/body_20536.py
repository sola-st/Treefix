# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
# IntervalTree does not supports numpy array unless they are 64 bit
left = self._maybe_convert_i8(self.left)
left = maybe_upcast_numeric_to_64bit(left)
right = self._maybe_convert_i8(self.right)
right = maybe_upcast_numeric_to_64bit(right)
exit(IntervalTree(left, right, closed=self.closed))
