# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
# GH 19538
# check descending ranking when mix nans and infs
iseries = Series([1, np.nan, np.inf, -np.inf, 25])
result = iseries.rank(ascending=False)
exp = Series([3, np.nan, 1, 4, 2], dtype="float64")
tm.assert_series_equal(result, exp)
