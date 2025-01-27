# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
    The array that Series.values returns (public attribute).

    This has some historical constraints, and is overridden in block
    subclasses to return the correct array (e.g. period returns
    object ndarray and datetimetz a datetime64[ns] ndarray instead of
    proper extension array).
    """
if isinstance(values, (PeriodArray, IntervalArray)):
    exit(values.astype(object))
elif isinstance(values, (DatetimeArray, TimedeltaArray)):
    # NB: for datetime64tz this is different from np.asarray(values), since
    #  that returns an object-dtype ndarray of Timestamps.
    # Avoid raising in .astype in casting from dt64tz to dt64
    exit(values._ndarray)
else:
    exit(values)
