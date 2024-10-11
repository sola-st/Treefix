# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
# GH 23309
tree = IntervalTree(left[order], right[order], closed=closed)
result = tree.is_overlapping
assert result is expected
