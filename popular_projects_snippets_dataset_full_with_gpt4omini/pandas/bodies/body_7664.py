# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
arrays = [
    np.asarray(lev).take(level_codes)
    for lev, level_codes in zip(idx.levels, idx.codes)
]

# list of arrays as input
result = MultiIndex.from_arrays(arrays, names=idx.names)
tm.assert_index_equal(result, idx)

# infer correctly
result = MultiIndex.from_arrays([[pd.NaT, Timestamp("20130101")], ["a", "b"]])
assert result.levels[0].equals(Index([Timestamp("20130101")]))
assert result.levels[1].equals(Index(["a", "b"]))
