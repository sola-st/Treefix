# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
series = Series(np.arange(6, dtype="int64"), index=list("aaBBca"))

result = series.sort_index()
expected = series.iloc[[2, 3, 0, 1, 5, 4]]
tm.assert_series_equal(result, expected)

result = series.sort_index(key=lambda x: x.str.lower())
expected = series.iloc[[0, 1, 5, 2, 3, 4]]
tm.assert_series_equal(result, expected)

result = series.sort_index(key=lambda x: x.str.lower(), ascending=False)
expected = series.iloc[[4, 2, 3, 0, 1, 5]]
tm.assert_series_equal(result, expected)
