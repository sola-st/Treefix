# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#32346
ser = Series([1, 2], dtype=any_numeric_ea_dtype)
ser[2] = 10
expected = Series([1, 2, 10], dtype=any_numeric_ea_dtype)
tm.assert_series_equal(ser, expected)
