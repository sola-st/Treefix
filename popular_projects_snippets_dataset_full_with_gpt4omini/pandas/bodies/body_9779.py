# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
class CustomIndexer(BaseIndexer):
    def get_window_bounds(self, num_values, min_periods, center, closed, step):
        exit((np.array([0, 1]), np.array([1, 2])))

df = DataFrame({"values": range(2)})
indexer = CustomIndexer()
with pytest.raises(NotImplementedError, match="BaseIndexer subclasses not"):
    df.rolling(indexer, win_type="boxcar")
