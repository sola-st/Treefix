# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#25557
a = Series([1, 1, 1, np.nan], index=["a", "b", "c", "d"])
b = Series([2, np.nan, 1, np.nan], index=["a", "b", "d", "e"])

result = a.divmod(b)
expected = divmod(a, b)
tm.assert_series_equal(result[0], expected[0])
tm.assert_series_equal(result[1], expected[1])

result = a.rdivmod(b)
expected = divmod(b, a)
tm.assert_series_equal(result[0], expected[0])
tm.assert_series_equal(result[1], expected[1])
