# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH#11339
# comparisons vs tuple
s = Series([(1, 1), (1, 2)])

result = s == (1, 2)
expected = Series([False, True])
tm.assert_series_equal(result, expected)

result = s != (1, 2)
expected = Series([True, False])
tm.assert_series_equal(result, expected)

result = s == (0, 0)
expected = Series([False, False])
tm.assert_series_equal(result, expected)

result = s != (0, 0)
expected = Series([True, True])
tm.assert_series_equal(result, expected)

s = Series([(1, 1), (1, 1)])

result = s == (1, 1)
expected = Series([True, True])
tm.assert_series_equal(result, expected)

result = s != (1, 1)
expected = Series([False, False])
tm.assert_series_equal(result, expected)
