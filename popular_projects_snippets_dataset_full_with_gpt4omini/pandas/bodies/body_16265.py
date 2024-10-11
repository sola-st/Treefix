# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 21987
expected = Series(["abc"])
result = Series("abc")
tm.assert_series_equal(result, expected)
