# Extracted from ./data/repos/pandas/pandas/core/arrays/_ranges.py
"""
    Generate a range of dates or timestamps with the spans between dates
    described by the given `freq` DateOffset.

    Parameters
    ----------
    start : Timedelta, Timestamp or None
        First point of produced date range.
    end : Timedelta, Timestamp or None
        Last point of produced date range.
    periods : int or None
        Number of periods in produced date range.
    freq : Tick
        Describes space between dates in produced date range.
    unit : str, default "ns"
        The resolution the output is meant to represent.

    Returns
    -------
    ndarray[np.int64]
        Representing the given resolution.
    """
istart = start.value if start is not None else None
iend = end.value if end is not None else None
freq.nanos  # raises if non-fixed frequency
td = Timedelta(freq)
try:
    td = td.as_unit(  # pyright: ignore[reportGeneralTypeIssues]
        unit, round_ok=False
    )
except ValueError as err:
    raise ValueError(
        f"freq={freq} is incompatible with unit={unit}. "
        "Use a lower freq or a higher unit instead."
    ) from err
stride = int(td.value)

if periods is None and istart is not None and iend is not None:
    b = istart
    # cannot just use e = Timestamp(end) + 1 because arange breaks when
    # stride is too large, see GH10887
    e = b + (iend - b) // stride * stride + stride // 2 + 1
elif istart is not None and periods is not None:
    b = istart
    e = _generate_range_overflow_safe(b, periods, stride, side="start")
elif iend is not None and periods is not None:
    e = iend + stride
    b = _generate_range_overflow_safe(e, periods, stride, side="end")
else:
    raise ValueError(
        "at least 'start' or 'end' should be specified if a 'period' is given."
    )

with np.errstate(over="raise"):
    # If the range is sufficiently large, np.arange may overflow
    #  and incorrectly return an empty array if not caught.
    try:
        values = np.arange(b, e, stride, dtype=np.int64)
    except FloatingPointError:
        xdr = [b]
        while xdr[-1] != e:
            xdr.append(xdr[-1] + stride)
        values = np.array(xdr[:-1], dtype=np.int64)
exit(values)
