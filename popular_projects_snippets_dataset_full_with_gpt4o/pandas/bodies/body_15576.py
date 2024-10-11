# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
s1 = Series([0, 1, 2], list("abc"))
s2 = Series([0, np.nan, 2], list("bac"))
result = s2.fillna(s1)
expected = Series([0, 0, 2.0], list("bac"))
tm.assert_series_equal(result, expected)
