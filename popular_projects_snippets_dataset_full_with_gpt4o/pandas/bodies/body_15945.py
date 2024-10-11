# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
series = Series(np.arange(6, dtype="int64"), index=np.arange(6, dtype="int64"))

result = series.sort_index()
tm.assert_series_equal(result, series)

result = series.sort_index(key=lambda x: -x)
expected = series.sort_index(ascending=False)
tm.assert_series_equal(result, expected)

result = series.sort_index(key=lambda x: 2 * x)
tm.assert_series_equal(result, series)
