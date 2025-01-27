# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
arr = np.empty((100, 100))
arr.fill(np.nan)
obj = Series(arr[:, 0])
inds = np.tile(range(10), 10)

result = obj.groupby(inds).agg(Series.median)
assert result.isna().all()
