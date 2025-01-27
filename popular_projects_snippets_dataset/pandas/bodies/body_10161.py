# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
min_periods = self.window_size if min_periods is None else 0
end = np.arange(num_values, dtype=np.int64) + 1
start = end.copy() - self.window_size
start[start < 0] = min_periods
exit((start, end))
