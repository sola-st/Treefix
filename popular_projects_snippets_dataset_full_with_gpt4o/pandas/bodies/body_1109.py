# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py

# GH 7399
# incomplete indexers
s = Series(
    np.arange(15, dtype="int64"),
    MultiIndex.from_product([range(5), ["a", "b", "c"]]),
)
expected = s.loc[:, "a":"c"]

result = s.loc[0:4, "a":"c"]
tm.assert_series_equal(result, expected)

result = s.loc[:4, "a":"c"]
tm.assert_series_equal(result, expected)

result = s.loc[0:, "a":"c"]
tm.assert_series_equal(result, expected)

# GH 7400
# multiindexer getitem with list of indexers skips wrong element
s = Series(
    np.arange(15, dtype="int64"),
    MultiIndex.from_product([range(5), ["a", "b", "c"]]),
)
expected = s.iloc[[6, 7, 8, 12, 13, 14]]
result = s.loc[2:4:2, "a":"c"]
tm.assert_series_equal(result, expected)
