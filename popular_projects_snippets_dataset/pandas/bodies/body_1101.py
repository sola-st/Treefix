# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH14730
# passing a series as a key with a MultiIndex
index = MultiIndex.from_product([[1, 2, 3], ["A", "B", "C"]])
x = Series(index=index, data=range(9), dtype=np.float64)
y = Series([1, 3])
expected = Series(
    data=[0, 1, 2, 6, 7, 8],
    index=MultiIndex.from_product([[1, 3], ["A", "B", "C"]]),
    dtype=np.float64,
)
result = x.loc[y]
tm.assert_series_equal(result, expected)

result = x.loc[[1, 3]]
tm.assert_series_equal(result, expected)

# GH15424
y1 = Series([1, 3], index=[1, 2])
result = x.loc[y1]
tm.assert_series_equal(result, expected)

empty = Series(data=[], dtype=np.float64)
expected = Series(
    [],
    index=MultiIndex(levels=index.levels, codes=[[], []], dtype=np.float64),
    dtype=np.float64,
)
result = x.loc[empty]
tm.assert_series_equal(result, expected)
