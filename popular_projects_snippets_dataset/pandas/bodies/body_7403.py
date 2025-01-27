# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_integrity.py
# non-smoke test that we don't get hash collisions

index = MultiIndex.from_product(
    [np.arange(1000), np.arange(1000)], names=["one", "two"]
)
result = index.get_indexer(index.values)
tm.assert_numpy_array_equal(result, np.arange(len(index), dtype="intp"))

for i in [0, 1, len(index) - 2, len(index) - 1]:
    result = index.get_loc(index[i])
    assert result == i
