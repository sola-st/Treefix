# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#47677
result = Series(["a", "b", "c"], dtype="category")
result.loc[3] = "a"
expected = Series(["a", "b", "c", "a"], dtype="category")
tm.assert_series_equal(result, expected)
