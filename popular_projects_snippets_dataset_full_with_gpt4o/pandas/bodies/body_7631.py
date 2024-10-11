# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH48384
idx = MultiIndex.from_arrays(
    [
        [2, 2, 1],
        [4, 5, 6],
    ]
)
result = idx.get_locs(keys)
expected = np.array(expected, dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
