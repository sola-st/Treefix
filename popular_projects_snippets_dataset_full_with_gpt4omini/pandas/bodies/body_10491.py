# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
# GH 10780
data = Series(np.random.rand(9), index=np.repeat([1, 2, 3], 3))
groupped = data.groupby(level=0)
result_false = groupped.filter(lambda x: x.mean() > 1, dropna=False)
expected_false = Series([np.nan] * 9, index=np.repeat([1, 2, 3], 3))
tm.assert_series_equal(result_false, expected_false)

result_true = groupped.filter(lambda x: x.mean() > 1, dropna=True)
expected_true = Series(index=pd.Index([], dtype=int), dtype=np.float64)
tm.assert_series_equal(result_true, expected_true)
