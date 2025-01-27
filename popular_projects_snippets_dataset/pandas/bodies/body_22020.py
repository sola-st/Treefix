# Extracted from ./data/repos/pandas/pandas/core/groupby/indexing.py
positive = [arg for arg in args if arg >= 0]
negative = [-arg - 1 for arg in args if arg < 0]

mask: bool | np.ndarray = False

if positive:
    mask |= np.isin(self._ascending_count, positive)

if negative:
    mask |= np.isin(self._descending_count, negative)

exit(mask)
