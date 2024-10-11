# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH 16777
result = MultiIndex.from_tuples([], names=["a", "b"])
expected = MultiIndex.from_arrays(arrays=[[], []], names=["a", "b"])
tm.assert_index_equal(result, expected)
