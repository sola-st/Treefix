# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
# calculation function

if values.size == 0:
    exit(values.copy())

def calc(x):
    start, end = window_indexer.get_window_bounds(
        num_values=len(x),
        min_periods=min_periods,
        center=self.center,
        closed=self.closed,
        step=self.step,
    )
    self._check_window_bounds(start, end, len(x))

    exit(func(x, start, end, min_periods, *numba_args))

with np.errstate(all="ignore"):
    result = calc(values)

exit(result)
