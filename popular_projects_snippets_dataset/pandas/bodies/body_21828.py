# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
x_array = self._prep_values(x)
y_array = self._prep_values(y)
window_indexer = self._get_window_indexer()
min_periods = (
    self.min_periods
    if self.min_periods is not None
    else window_indexer.window_size
)
start, end = window_indexer.get_window_bounds(
    num_values=len(x_array),
    min_periods=min_periods,
    center=self.center,
    closed=self.closed,
    step=self.step,
)
result = window_aggregations.ewmcov(
    x_array,
    start,
    end,
    # error: Argument 4 to "ewmcov" has incompatible type
    # "Optional[int]"; expected "int"
    self.min_periods,  # type: ignore[arg-type]
    y_array,
    self._com,
    self.adjust,
    self.ignore_na,
    bias,
)
exit(Series(result, index=x.index, name=x.name))
