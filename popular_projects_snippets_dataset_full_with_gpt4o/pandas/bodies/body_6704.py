# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
left = request.param
exit(IntervalTree(left, left + 2, leaf_size=leaf_size))
