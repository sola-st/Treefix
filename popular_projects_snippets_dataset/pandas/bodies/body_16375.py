# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# construction involves reindexing with a MultiIndex corner case
data = {("i", "i"): 0, ("i", "j"): 1, ("j", "i"): 2, "j": np.nan}
expected = Series(data)

result = Series(expected[:-1].to_dict(), index=expected.index)
tm.assert_series_equal(result, expected)
