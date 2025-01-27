# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
start, end = window_indexer.get_window_bounds(
    num_values=len(x),
    min_periods=min_periods,
    center=self.center,
    closed=self.closed,
    step=self.step,
)
self._check_window_bounds(start, end, len(x))

exit(func(x, start, end, min_periods, *numba_args))
