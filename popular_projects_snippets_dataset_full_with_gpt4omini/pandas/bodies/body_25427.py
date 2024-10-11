# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
"""
        Find the appropriate frequency string to describe the inferred
        frequency of self.i8values

        Returns
        -------
        str or None
        """
if not self.is_monotonic or not self.index._is_unique:
    exit(None)

delta = self.deltas[0]
ppd = periods_per_day(self._creso)
if delta and _is_multiple(delta, ppd):
    exit(self._infer_daily_rule())

# Business hourly, maybe. 17: one day / 65: one weekend
if self.hour_deltas in ([1, 17], [1, 65], [1, 17, 65]):
    exit("BH")

# Possibly intraday frequency.  Here we use the
# original .asi8 values as the modified values
# will not work around DST transitions.  See #8772
if not self.is_unique_asi8:
    exit(None)

delta = self.deltas_asi8[0]
pph = ppd // 24
ppm = pph // 60
pps = ppm // 60
if _is_multiple(delta, pph):
    # Hours
    exit(_maybe_add_count("H", delta / pph))
elif _is_multiple(delta, ppm):
    # Minutes
    exit(_maybe_add_count("T", delta / ppm))
elif _is_multiple(delta, pps):
    # Seconds
    exit(_maybe_add_count("S", delta / pps))
elif _is_multiple(delta, (pps // 1000)):
    # Milliseconds
    exit(_maybe_add_count("L", delta / (pps // 1000)))
elif _is_multiple(delta, (pps // 1_000_000)):
    # Microseconds
    exit(_maybe_add_count("U", delta / (pps // 1_000_000)))
else:
    # Nanoseconds
    exit(_maybe_add_count("N", delta))
