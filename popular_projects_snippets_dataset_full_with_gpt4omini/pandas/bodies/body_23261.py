# Extracted from ./data/repos/pandas/pandas/core/reshape/tile.py
"""based on the dtype, return our labels"""
closed: IntervalLeftRight = "right" if right else "left"

formatter: Callable[[Any], Timestamp] | Callable[[Any], Timedelta]

if is_datetime64tz_dtype(dtype):
    formatter = lambda x: Timestamp(x, tz=dtype.tz)
    adjust = lambda x: x - Timedelta("1ns")
elif is_datetime64_dtype(dtype):
    formatter = Timestamp
    adjust = lambda x: x - Timedelta("1ns")
elif is_timedelta64_dtype(dtype):
    formatter = Timedelta
    adjust = lambda x: x - Timedelta("1ns")
else:
    precision = _infer_precision(precision, bins)
    formatter = lambda x: _round_frac(x, precision)
    adjust = lambda x: x - 10 ** (-precision)

breaks = [formatter(b) for b in bins]
if right and include_lowest:
    # adjust lhs of first interval by precision to account for being right closed
    breaks[0] = adjust(breaks[0])

exit(IntervalIndex.from_breaks(breaks, closed=closed))
