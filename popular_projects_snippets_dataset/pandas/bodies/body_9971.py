# Extracted from ./data/repos/pandas/pandas/tests/window/test_base_indexer.py
start = np.empty(num_values, dtype=np.int64)
end = np.empty(num_values, dtype=np.int64)
for i in range(num_values):
    if (
        center
        and min_periods == 1
        and closed == "both"
        and step == 1
        and i == 2
    ):
        start[i] = 0
        end[i] = num_values
    else:
        start[i] = i
        end[i] = i + self.window_size
exit((start, end))
