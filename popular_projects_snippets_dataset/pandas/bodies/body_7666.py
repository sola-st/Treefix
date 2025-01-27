# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
arrays = tuple(
    tuple(np.asarray(lev).take(level_codes))
    for lev, level_codes in zip(idx.levels, idx.codes)
)

# tuple of tuples as input
result = MultiIndex.from_arrays(arrays, names=idx.names)
tm.assert_index_equal(result, idx)
