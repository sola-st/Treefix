# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
"""
    If both a dtype and a freq are available, ensure they match.  If only
    dtype is available, extract the implied freq.

    Parameters
    ----------
    dtype : dtype
    freq : DateOffset or None

    Returns
    -------
    freq : DateOffset

    Raises
    ------
    ValueError : non-period dtype
    IncompatibleFrequency : mismatch between dtype and freq
    """
if freq is not None:
    # error: Incompatible types in assignment (expression has type
    # "BaseOffset", variable has type "Union[BaseOffsetT, timedelta,
    # str, None]")
    freq = to_offset(freq)  # type: ignore[assignment]

if dtype is not None:
    dtype = pandas_dtype(dtype)
    if not is_period_dtype(dtype):
        raise ValueError("dtype must be PeriodDtype")
    if freq is None:
        freq = dtype.freq
    elif freq != dtype.freq:
        raise IncompatibleFrequency("specified freq and dtype are different")
    # error: Incompatible return value type (got "Union[BaseOffset, Any, None]",
    # expected "BaseOffset")
exit(freq)  # type: ignore[return-value]
