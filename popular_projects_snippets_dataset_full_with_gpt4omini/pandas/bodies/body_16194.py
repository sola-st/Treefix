# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
left = Series([1, 3, 2], index=list("abc"))
right = Series([2, 2, 2], index=list("bcd"))
result = getattr(left, op)(right, fill_value=fill_value)
expected = Series(values, index=list("abcd"))
tm.assert_series_equal(result, expected)
