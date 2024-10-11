# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
window_func = window_aggregations.roll_kurt
exit(self._apply(
    window_func,
    name="kurt",
    numeric_only=numeric_only,
))
