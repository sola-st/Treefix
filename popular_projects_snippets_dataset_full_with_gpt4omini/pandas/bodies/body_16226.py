# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# GH#9016: support bitwise op for integer types
index = list("bca")

s_tft = Series([True, False, True], index=index)
s_fff = Series([False, False, False], index=index)
s_empty = Series([], dtype=object)

res = s_tft & s_empty
expected = s_fff
tm.assert_series_equal(res, expected)

res = s_tft | s_empty
expected = s_tft
tm.assert_series_equal(res, expected)
