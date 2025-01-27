# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
# GH 46658

tree = IntervalTree(left * 101, right * 101)

result = tree.root.pivot
assert result == expected
