# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
start = np.empty(num_values, dtype=np.int64)
end = np.empty(num_values, dtype=np.int64)
for i in range(num_values):
    if self.use_expanding[i]:
        start[i] = 0
        end[i] = i + 1
    else:
        start[i] = i
        end[i] = i + self.window_size
exit((start, end))
