# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# using an ndarray like function
s = Series(np.random.randn(10))
result = Series(np.ones_like(s))
expected = Series(1, index=range(10), dtype="float64")
tm.assert_series_equal(result, expected)
