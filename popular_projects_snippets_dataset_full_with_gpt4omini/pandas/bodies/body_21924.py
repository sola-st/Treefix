# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
window_func = partial(
    window_aggregations.roll_rank,
    method=method,
    ascending=ascending,
    percentile=pct,
)

exit(self._apply(window_func, name="rank", numeric_only=numeric_only))
