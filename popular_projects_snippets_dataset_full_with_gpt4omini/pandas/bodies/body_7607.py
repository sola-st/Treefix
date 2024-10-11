# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
index = MultiIndex(
    levels=[Index(np.arange(4)), Index(np.arange(4)), Index(np.arange(4))],
    codes=[
        np.array([0, 0, 1, 2, 2, 2, 3, 3]),
        np.array([0, 1, 0, 0, 0, 1, 0, 1]),
        np.array([1, 0, 1, 1, 0, 0, 1, 0]),
    ],
)
loc, new_index = index.get_loc_level((0, 1))
expected = slice(1, 2)
exp_index = index[expected].droplevel(0).droplevel(0)
assert loc == expected
assert new_index.equals(exp_index)

loc, new_index = index.get_loc_level((0, 1, 0))
expected = 1
assert loc == expected
assert new_index is None

with pytest.raises(KeyError, match=r"^\(2, 2\)$"):
    index.get_loc_level((2, 2))
# GH 22221: unused label
with pytest.raises(KeyError, match=r"^2$"):
    index.drop(2).get_loc_level(2)
# Unused label on unsorted level:
with pytest.raises(KeyError, match=r"^2$"):
    index.drop(1, level=2).get_loc_level(2, level=2)

index = MultiIndex(
    levels=[[2000], list(range(4))],
    codes=[np.array([0, 0, 0, 0]), np.array([0, 1, 2, 3])],
)
result, new_index = index.get_loc_level((2000, slice(None, None)))
expected = slice(None, None)
assert result == expected
assert new_index.equals(index.droplevel(0))
