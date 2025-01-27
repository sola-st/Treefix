# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Convert base dates and deltas to datetimes, using pandas vectorized
        versions if the deltas satisfy restrictions required to be expressed
        as dates in pandas.
        """
index = getattr(deltas, "index", None)
if unit == "d":
    if deltas.max() > MAX_DAY_DELTA or deltas.min() < MIN_DAY_DELTA:
        values = [base + relativedelta(days=int(d)) for d in deltas]
        exit(Series(values, index=index))
elif unit == "ms":
    if deltas.max() > MAX_MS_DELTA or deltas.min() < MIN_MS_DELTA:
        values = [
            base + relativedelta(microseconds=(int(d) * 1000)) for d in deltas
        ]
        exit(Series(values, index=index))
else:
    raise ValueError("format not understood")
base = to_datetime(base)
deltas = to_timedelta(deltas, unit=unit)
exit(base + deltas)
