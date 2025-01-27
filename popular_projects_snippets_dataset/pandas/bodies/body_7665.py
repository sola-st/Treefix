# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH 18434
arrays = [
    np.asarray(lev).take(level_codes)
    for lev, level_codes in zip(idx.levels, idx.codes)
]

# iterator as input
result = MultiIndex.from_arrays(iter(arrays), names=idx.names)
tm.assert_index_equal(result, idx)

# invalid iterator input
msg = "Input must be a list / sequence of array-likes."
with pytest.raises(TypeError, match=msg):
    MultiIndex.from_arrays(0)
