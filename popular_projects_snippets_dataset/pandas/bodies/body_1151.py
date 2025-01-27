# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 19517
idx = MultiIndex.from_product([["a", "b"], ["A", "B"]], names=[1, 0])
s2 = Series(index=idx, dtype=np.float64)
result = s2.loc["a"]
expected = Series([np.nan, np.nan], index=Index(["A", "B"], name=0))
tm.assert_series_equal(result, expected)
