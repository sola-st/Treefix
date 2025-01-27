# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 15289
s = pd.Series(list("abcd"))
tm.assert_series_equal(s, s.replace({}))

empty_series = pd.Series([])
tm.assert_series_equal(s, s.replace(empty_series))
