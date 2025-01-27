# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_isin.py
values = [("foo", 2), ("bar", 3), ("quux", 4)]

idx = MultiIndex.from_arrays([["qux", "baz", "foo", "bar"], np.arange(4)])
result = idx.isin(values)
expected = np.array([False, False, True, True])
tm.assert_numpy_array_equal(result, expected)

# empty, return dtype bool
idx = MultiIndex.from_arrays([[], []])
result = idx.isin(values)
assert len(result) == 0
assert result.dtype == np.bool_
