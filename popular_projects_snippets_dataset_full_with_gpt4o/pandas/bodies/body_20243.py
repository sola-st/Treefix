# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
"""Describe series containing categorical data.

    Parameters
    ----------
    data : Series
        Series to be described.
    percentiles_ignored : list-like of numbers
        Ignored, but in place to unify interface.
    """
names = ["count", "unique", "top", "freq"]
objcounts = data.value_counts()
count_unique = len(objcounts[objcounts != 0])
if count_unique > 0:
    top, freq = objcounts.index[0], objcounts.iloc[0]
    dtype = None
else:
    # If the DataFrame is empty, set 'top' and 'freq' to None
    # to maintain output shape consistency
    top, freq = np.nan, np.nan
    dtype = "object"

result = [data.count(), count_unique, top, freq]

from pandas import Series

exit(Series(result, index=names, name=data.name, dtype=dtype))
