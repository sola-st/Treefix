# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH 25616
# casts to object without Exception from OverflowError
s = pd.Series([0, 1, 2, 3, 4])
result = s.replace([3], ["100000000000000000000"])
expected = pd.Series([0, 1, 2, "100000000000000000000", 4])
tm.assert_series_equal(result, expected)

s = pd.Series([0, "100000000000000000000", "100000000000000000001"])
result = s.replace(["100000000000000000000"], [1])
expected = pd.Series([0, 1, "100000000000000000001"])
tm.assert_series_equal(result, expected)
