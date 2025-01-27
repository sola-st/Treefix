# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
mi = MultiIndex(
    levels=[["b", "d", "a"], [1, 2, 3]],
    codes=[[0, 1, 0, 2], [2, 0, 0, 1]],
    names=["col1", "col2"],
)
recons = mi._sort_levels_monotonic()

# These are equal.
assert mi.equals(recons)
assert Index(mi.values).equals(Index(recons.values))
