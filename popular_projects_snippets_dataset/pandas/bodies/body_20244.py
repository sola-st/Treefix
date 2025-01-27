# Extracted from ./data/repos/pandas/pandas/core/methods/describe.py
"""Describe series containing timestamp data treated as categorical.

    Parameters
    ----------
    data : Series
        Series to be described.
    percentiles_ignored : list-like of numbers
        Ignored, but in place to unify interface.
    """
names = ["count", "unique"]
objcounts = data.value_counts()
count_unique = len(objcounts[objcounts != 0])
result = [data.count(), count_unique]
dtype = None
if count_unique > 0:
    top, freq = objcounts.index[0], objcounts.iloc[0]
    tz = data.dt.tz
    asint = data.dropna().values.view("i8")
    top = Timestamp(top)
    if top.tzinfo is not None and tz is not None:
        # Don't tz_localize(None) if key is already tz-aware
        top = top.tz_convert(tz)
    else:
        top = top.tz_localize(tz)
    names += ["top", "freq", "first", "last"]
    result += [
        top,
        freq,
        Timestamp(asint.min(), tz=tz),
        Timestamp(asint.max(), tz=tz),
    ]

# If the DataFrame is empty, set 'top' and 'freq' to None
# to maintain output shape consistency
else:
    names += ["top", "freq"]
    result += [np.nan, np.nan]
    dtype = "object"

from pandas import Series

exit(Series(result, index=names, name=data.name, dtype=dtype))
