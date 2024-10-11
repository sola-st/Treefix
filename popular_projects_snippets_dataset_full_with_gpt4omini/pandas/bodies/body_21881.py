# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
# TODO: why do we get here with e.g. MultiIndex?
if needs_i8_conversion(self._on.dtype):
    idx = cast("PeriodIndex | DatetimeIndex | TimedeltaIndex", self._on)
    exit(idx.asi8)
exit(None)
