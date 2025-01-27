# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
window_func = window_aggregations.roll_skew
exit(self._apply(
    window_func,
    name="skew",
    numeric_only=numeric_only,
))
