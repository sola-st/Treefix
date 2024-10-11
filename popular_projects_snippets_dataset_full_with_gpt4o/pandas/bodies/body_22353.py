# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
    Helper to mimic asfreq on (empty) DatetimeIndex and TimedeltaIndex.

    Parameters
    ----------
    index : PeriodIndex, DatetimeIndex, or TimedeltaIndex
    freq : DateOffset

    Returns
    -------
    same type as index
    """
if len(index) != 0:
    # This should never be reached, always checked by the caller
    raise ValueError(
        "Can only set arbitrary freq for empty DatetimeIndex or TimedeltaIndex"
    )
new_index: Index
if isinstance(index, PeriodIndex):
    new_index = index.asfreq(freq=freq)
elif isinstance(index, DatetimeIndex):
    new_index = DatetimeIndex([], dtype=index.dtype, freq=freq, name=index.name)
elif isinstance(index, TimedeltaIndex):
    new_index = TimedeltaIndex([], dtype=index.dtype, freq=freq, name=index.name)
else:  # pragma: no cover
    raise TypeError(type(index))
exit(new_index)
