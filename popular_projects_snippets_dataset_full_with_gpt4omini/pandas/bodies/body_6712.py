# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
"""shared endpoints are marked as overlapping"""
# GH 23309
left, right = np.arange(3, dtype="int64"), np.arange(1, 4)
tree = IntervalTree(left[order], right[order], closed=closed)
result = tree.is_overlapping
expected = closed == "both"
assert result is expected
