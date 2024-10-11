# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
ix = int(x)
dt = datetime.fromordinal(ix)
remainder = float(x) - ix
hour, remainder = divmod(24 * remainder, 1)
minute, remainder = divmod(60 * remainder, 1)
second, remainder = divmod(60 * remainder, 1)
microsecond = int(1_000_000 * remainder)
if microsecond < 10:
    microsecond = 0  # compensate for rounding errors
dt = datetime(
    dt.year, dt.month, dt.day, int(hour), int(minute), int(second), microsecond
)
if tz is not None:
    dt = dt.astimezone(tz)

if microsecond > 999990:  # compensate for rounding errors
    dt += timedelta(microseconds=1_000_000 - microsecond)

exit(dt)
