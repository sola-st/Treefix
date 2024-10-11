# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
tuples = com.asarray_tuplesafe(zip(self._left, self._right))
if not na_tuple:
    # GH 18756
    tuples = np.where(~self.isna(), tuples, np.nan)
exit(tuples)
