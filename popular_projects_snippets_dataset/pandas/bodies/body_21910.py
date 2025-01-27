# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
if not raw:
    # GH 45912
    values = Series(values, index=self._on)
exit(window_func(values, begin, end, min_periods))
