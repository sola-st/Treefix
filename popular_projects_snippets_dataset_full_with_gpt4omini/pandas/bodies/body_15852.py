# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
s = pd.Series([True, False, True])
result = s.replace("fun", "in-the-sun")
tm.assert_series_equal(s, result)
