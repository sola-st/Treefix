# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
s = pd.Series([True, False, True])
result = s.replace(True, False)
expected = pd.Series([False] * len(s))
tm.assert_series_equal(expected, result)
