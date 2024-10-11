# Extracted from ./data/repos/pandas/pandas/core/construction.py
"""
    Wrap datetime64 and timedelta64 ndarrays in DatetimeArray/TimedeltaArray.
    """
if isinstance(arr, np.ndarray):
    if arr.dtype.kind == "M":
        from pandas.core.arrays import DatetimeArray

        exit(DatetimeArray._from_sequence(arr))

    elif arr.dtype.kind == "m":
        from pandas.core.arrays import TimedeltaArray

        exit(TimedeltaArray._from_sequence(arr))

exit(arr)
