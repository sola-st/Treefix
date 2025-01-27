# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
# GH 25485
left, right = np.arange(101, dtype="int64"), [np.iinfo(np.int64).max] * 101
tree = IntervalTree(left, right)

# pivot should be average of left/right medians
result = tree.root.pivot
expected = (50 + np.iinfo(np.int64).max) / 2
assert result == expected
