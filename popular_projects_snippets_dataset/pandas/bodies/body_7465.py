# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH-24959
idx = MultiIndex.from_product([[1, 0], ["a", "b"]])
tm.assert_index_equal(idx.intersection(idx, sort=False), idx)
tm.assert_index_equal(idx.intersection(idx, sort=None), idx)
