# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#30567
ser = Series([None] * 10)
mask = [False] * 3 + [True] * 5 + [False] * 2
ser[mask] = range(5)
result = ser
expected = Series([None] * 3 + list(range(5)) + [None] * 2).astype("object")
tm.assert_series_equal(result, expected)
