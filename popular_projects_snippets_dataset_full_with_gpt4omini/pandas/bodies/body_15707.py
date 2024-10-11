# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_compare.py
# We want to make sure the relevant NaNs do not get dropped
s1 = pd.Series(["a", "b", "c"])
s2 = pd.Series(["x", "b", np.nan])

result = s1.compare(s2, align_axis=0)

indices = pd.MultiIndex.from_product([[0, 2], ["self", "other"]])
expected = pd.Series(["a", "x", "c", np.nan], index=indices)
tm.assert_series_equal(result, expected)
