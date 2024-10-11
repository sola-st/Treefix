# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# #16844
a = MultiIndex(levels=[[], []], codes=[[], []], names=["a", "b"])
b = MultiIndex.from_arrays(arrays=[[], []], names=["a", "b"])
tm.assert_index_equal(a, b)
