# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
# GH 23309
tree = IntervalTree(left, right, closed=closed)
assert tree.is_overlapping is False
