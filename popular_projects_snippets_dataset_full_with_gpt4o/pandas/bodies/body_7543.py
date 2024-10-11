# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reshape.py
reps = 2
numbers = [1, 2, 3]
names = np.array(["foo", "bar"])

m = MultiIndex.from_product([numbers, names], names=names)
expected = MultiIndex.from_product([numbers, names.repeat(reps)], names=names)
tm.assert_index_equal(m.repeat(reps), expected)
