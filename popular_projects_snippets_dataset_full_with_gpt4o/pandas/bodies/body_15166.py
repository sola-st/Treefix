# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
# GH#45263
ser = Series([1, 2, 3, 4], [True, None, np.nan, pd.NaT])
result = repr(ser)
expected = "True    1\nNone    2\nNaN     3\nNaT     4\ndtype: int64"
assert result == expected
