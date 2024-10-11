# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_quantile.py
result = Series([1, 2, 3], dtype=dtype).quantile(np.arange(0, 1, 0.25))
expected = Series(np.arange(1, 3, 0.5), index=np.arange(0, 1, 0.25))
if dtype == "Int64":
    expected = expected.astype("Float64")
tm.assert_series_equal(result, expected)
