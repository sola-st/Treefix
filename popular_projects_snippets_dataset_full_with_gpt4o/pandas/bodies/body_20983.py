# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
# using the specific numpy integer instead of python int to get
#  the correct dtype back from _quantile in the all-NA case
dtype = self._ndarray.dtype
exit(dtype.type(-1))
