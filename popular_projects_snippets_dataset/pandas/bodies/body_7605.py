# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
assert idx.get_loc(("foo", "two")) == 1
assert idx.get_loc(("baz", "two")) == 3
with pytest.raises(KeyError, match=r"^15$"):
    idx.get_loc(("bar", "two"))
with pytest.raises(KeyError, match=r"^'quux'$"):
    idx.get_loc("quux")

# 3 levels
index = MultiIndex(
    levels=[Index(np.arange(4)), Index(np.arange(4)), Index(np.arange(4))],
    codes=[
        np.array([0, 0, 1, 2, 2, 2, 3, 3]),
        np.array([0, 1, 0, 0, 0, 1, 0, 1]),
        np.array([1, 0, 1, 1, 0, 0, 1, 0]),
    ],
)
with pytest.raises(KeyError, match=r"^\(1, 1\)$"):
    index.get_loc((1, 1))
assert index.get_loc((2, 0)) == slice(3, 5)
