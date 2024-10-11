# Extracted from ./data/repos/pandas/pandas/tests/window/test_base_indexer.py
df = DataFrame({"values": range(5)})

class CustomIndexer(BaseIndexer):
    def get_window_bounds(self, num_values, min_periods, center, closed, step):
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

indexer = CustomIndexer(window_size=1)
result = df.rolling(
    indexer, center=True, min_periods=1, closed="both", step=1
).sum()
expected = DataFrame({"values": [0.0, 1.0, 10.0, 3.0, 4.0]})
tm.assert_frame_equal(result, expected)
