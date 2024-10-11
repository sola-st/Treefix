# Extracted from ./data/repos/pandas/pandas/tests/window/test_base_indexer.py
class CustomIndexer(BaseIndexer):
    def get_window_bounds(self, num_values, min_periods, center, closed, step):
        exit((np.array([1]), np.array([1, 2])))

indexer = CustomIndexer()
roll = Series(1).rolling(indexer)
match = "start"
with pytest.raises(ValueError, match=match):
    roll.mean()

with pytest.raises(ValueError, match=match):
    next(iter(roll))

with pytest.raises(ValueError, match=match):
    roll.corr(pairwise=True)

with pytest.raises(ValueError, match=match):
    roll.cov(pairwise=True)
