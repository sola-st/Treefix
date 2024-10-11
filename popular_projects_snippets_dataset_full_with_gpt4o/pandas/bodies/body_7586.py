# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# some searchsorted action

index = MultiIndex(
    levels=[[0, 2, 4, 6], [0, 2, 4]],
    codes=[[0, 0, 0, 1, 1, 2, 3, 3, 3], [0, 1, 2, 1, 2, 2, 0, 1, 2]],
)

result = index.slice_locs((1, 0), (5, 2))
assert result == (3, 6)

result = index.slice_locs(1, 5)
assert result == (3, 6)

result = index.slice_locs((2, 2), (5, 2))
assert result == (3, 6)

result = index.slice_locs(2, 5)
assert result == (3, 6)

result = index.slice_locs((1, 0), (6, 3))
assert result == (3, 8)

result = index.slice_locs(-1, 10)
assert result == (0, len(index))
