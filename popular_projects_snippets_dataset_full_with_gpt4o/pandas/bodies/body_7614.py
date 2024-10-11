# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# TODO: de-duplicate with test_get_loc_duplicates above?
index = MultiIndex(
    levels=[["D", "B", "C"], [0, 26, 27, 37, 57, 67, 75, 82]],
    codes=[[0, 0, 0, 1, 2, 2, 2, 2, 2, 2], [1, 3, 4, 6, 0, 2, 2, 3, 5, 7]],
    names=["tag", "day"],
)

assert index.get_loc("D") == slice(0, 3)
