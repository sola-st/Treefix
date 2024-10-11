# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
"""
        Return a new IntervalArray with the replacement attributes

        Parameters
        ----------
        left : Index
            Values to be used for the left-side of the intervals.
        right : Index
            Values to be used for the right-side of the intervals.
        """
dtype = IntervalDtype(left.dtype, closed=self.closed)
left, right, dtype = self._ensure_simple_new_inputs(left, right, dtype=dtype)
self._validate(left, right, dtype=dtype)

exit(self._simple_new(left, right, dtype=dtype))
