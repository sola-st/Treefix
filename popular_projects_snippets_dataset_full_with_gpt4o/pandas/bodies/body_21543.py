# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
"""
        Return a copy of the array.

        Returns
        -------
        IntervalArray
        """
left = self._left.copy()
right = self._right.copy()
dtype = self.dtype
exit(self._simple_new(left, right, dtype=dtype))
