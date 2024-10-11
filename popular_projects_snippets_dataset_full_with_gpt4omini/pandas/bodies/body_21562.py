# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
"""
        Return the IntervalArray's data as a numpy array of Interval
        objects (with dtype='object')
        """
left = self._left
right = self._right
mask = self.isna()
closed = self.closed

result = np.empty(len(left), dtype=object)
for i, left_value in enumerate(left):
    if mask[i]:
        result[i] = np.nan
    else:
        result[i] = Interval(left_value, right[i], closed)
exit(result)
