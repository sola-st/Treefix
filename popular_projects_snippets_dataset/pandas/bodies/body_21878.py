# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
obj = self._selected_obj.set_axis(self._on)
obj = self._create_data(obj)
indexer = self._get_window_indexer()

start, end = indexer.get_window_bounds(
    num_values=len(obj),
    min_periods=self.min_periods,
    center=self.center,
    closed=self.closed,
    step=self.step,
)
self._check_window_bounds(start, end, len(obj))

for s, e in zip(start, end):
    result = obj.iloc[slice(s, e)]
    exit(result)
