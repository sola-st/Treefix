# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_astype.py
expected = idx.copy()
actual = idx.astype("O")
tm.assert_copy(actual.levels, expected.levels)
tm.assert_copy(actual.codes, expected.codes)
assert actual.names == list(expected.names)

with pytest.raises(TypeError, match="^Setting.*dtype.*object"):
    idx.astype(np.dtype(int))
