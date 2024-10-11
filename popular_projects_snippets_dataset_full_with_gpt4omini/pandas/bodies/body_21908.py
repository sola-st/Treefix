# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
window_func = window_aggregations.roll_sum
exit(self._apply(window_func, name="count", numeric_only=numeric_only))
