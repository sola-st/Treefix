# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# https://github.com/pandas-dev/pandas/issues/21390
midx = MultiIndex.from_product(
    [
        Categorical(["a", "b", "c"]),
        Categorical(date_range("2012-01-01", periods=3, freq="H")),
    ]
)
result = midx.get_indexer(midx)
tm.assert_numpy_array_equal(result, np.arange(9, dtype=np.intp))
