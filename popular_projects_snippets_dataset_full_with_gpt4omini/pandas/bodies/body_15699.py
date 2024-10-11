# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_values.py
series = Series(np.array(["Hello", "goodbye"]))

result = series.sort_values(axis=0)
expected = series
tm.assert_series_equal(result, expected)

result = series.sort_values(axis=0, key=lambda x: x.str.lower())
expected = series[::-1]
tm.assert_series_equal(result, expected)
