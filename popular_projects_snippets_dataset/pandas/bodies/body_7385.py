# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_sorting.py
mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list("ABC"))
sorted_idx, _ = mi.sortlevel("A", sort_remaining=False)
assert sorted_idx.equals(mi)
