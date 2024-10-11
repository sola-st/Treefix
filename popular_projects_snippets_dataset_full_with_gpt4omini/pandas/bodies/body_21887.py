# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Apply the given pairwise function given 2 pandas objects (DataFrame/Series)
        """
target = self._create_data(target, numeric_only)
if other is None:
    other = target
    # only default unset
    pairwise = True if pairwise is None else pairwise
elif not isinstance(other, (ABCDataFrame, ABCSeries)):
    raise ValueError("other must be a DataFrame or Series")
elif other.ndim == 2 and numeric_only:
    other = self._make_numeric_only(other)

exit(flex_binary_moment(target, other, func, pairwise=bool(pairwise)))
