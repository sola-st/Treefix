# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH15434
# passing an array as a key with a MultiIndex
index = MultiIndex.from_product([[1, 2, 3], ["A", "B", "C"]])
x = Series(index=index, data=range(9), dtype=np.float64)
y = np.array([1, 3])
expected = Series(
    data=[0, 1, 2, 6, 7, 8],
    index=MultiIndex.from_product([[1, 3], ["A", "B", "C"]]),
    dtype=np.float64,
)
result = x.loc[y]
tm.assert_series_equal(result, expected)

# empty array:
empty = np.array([])
expected = Series(
    [],
    index=MultiIndex(levels=index.levels, codes=[[], []], dtype=np.float64),
    dtype="float64",
)
result = x.loc[empty]
tm.assert_series_equal(result, expected)

# 0-dim array (scalar):
scalar = np.int64(1)
expected = Series(data=[0, 1, 2], index=["A", "B", "C"], dtype=np.float64)
result = x.loc[scalar]
tm.assert_series_equal(result, expected)
