# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# GH#9016: support bitwise op for integer types
s_0123 = Series(range(4), dtype="int64")

expected = Series([False] * 4)

result = s_0123 & False
tm.assert_series_equal(result, expected)

result = s_0123 & [False]
tm.assert_series_equal(result, expected)

result = s_0123 & (False,)
tm.assert_series_equal(result, expected)

result = s_0123 ^ False
expected = Series([False, True, True, True])
tm.assert_series_equal(result, expected)
