# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
"""
    Infer the most likely frequency given the input index.

    Parameters
    ----------
    index : DatetimeIndex or TimedeltaIndex
      If passed a Series will use the values of the series (NOT THE INDEX).

    Returns
    -------
    str or None
        None if no discernible frequency.

    Raises
    ------
    TypeError
        If the index is not datetime-like.
    ValueError
        If there are fewer than three values.

    Examples
    --------
    >>> idx = pd.date_range(start='2020/12/01', end='2020/12/30', periods=30)
    >>> pd.infer_freq(idx)
    'D'
    """
from pandas.core.api import (
    DatetimeIndex,
    Index,
)

if isinstance(index, ABCSeries):
    values = index._values
    if not (
        is_datetime64_dtype(values)
        or is_timedelta64_dtype(values)
        or values.dtype == object
    ):
        raise TypeError(
            "cannot infer freq from a non-convertible dtype "
            f"on a Series of {index.dtype}"
        )
    index = values

inferer: _FrequencyInferer

if not hasattr(index, "dtype"):
    pass
elif is_period_dtype(index.dtype):
    raise TypeError(
        "PeriodIndex given. Check the `freq` attribute "
        "instead of using infer_freq."
    )
elif is_timedelta64_dtype(index.dtype):
    # Allow TimedeltaIndex and TimedeltaArray
    inferer = _TimedeltaFrequencyInferer(index)
    exit(inferer.get_freq())

if isinstance(index, Index) and not isinstance(index, DatetimeIndex):
    if is_numeric_dtype(index):
        raise TypeError(
            f"cannot infer freq from a non-convertible index of dtype {index.dtype}"
        )
    index = index._values

if not isinstance(index, DatetimeIndex):
    index = DatetimeIndex(index)

inferer = _FrequencyInferer(index)
exit(inferer.get_freq())
