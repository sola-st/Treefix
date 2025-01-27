# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_equivalence.py
assert idx.equals(idx)
assert not idx.equals(idx.values)
assert idx.equals(Index(idx.values))

assert idx.equal_levels(idx)
assert not idx.equals(idx[:-1])
assert not idx.equals(idx[-1])

# different number of levels
index = MultiIndex(
    levels=[Index(list(range(4))), Index(list(range(4))), Index(list(range(4)))],
    codes=[
        np.array([0, 0, 1, 2, 2, 2, 3, 3]),
        np.array([0, 1, 0, 0, 0, 1, 0, 1]),
        np.array([1, 0, 1, 1, 0, 0, 1, 0]),
    ],
)

index2 = MultiIndex(levels=index.levels[:-1], codes=index.codes[:-1])
assert not index.equals(index2)
assert not index.equal_levels(index2)

# levels are different
major_axis = Index(list(range(4)))
minor_axis = Index(list(range(2)))

major_codes = np.array([0, 0, 1, 2, 2, 3])
minor_codes = np.array([0, 1, 0, 0, 1, 0])

index = MultiIndex(
    levels=[major_axis, minor_axis], codes=[major_codes, minor_codes]
)
assert not idx.equals(index)
assert not idx.equal_levels(index)

# some of the labels are different
major_axis = Index(["foo", "bar", "baz", "qux"])
minor_axis = Index(["one", "two"])

major_codes = np.array([0, 0, 2, 2, 3, 3])
minor_codes = np.array([0, 1, 0, 1, 0, 1])

index = MultiIndex(
    levels=[major_axis, minor_axis], codes=[major_codes, minor_codes]
)
assert not idx.equals(index)
