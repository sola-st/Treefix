# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# see GH#16991
s = Series(["a", "b"])
expected = Series([False, False])

result = s.isin(empty)
tm.assert_series_equal(expected, result)
