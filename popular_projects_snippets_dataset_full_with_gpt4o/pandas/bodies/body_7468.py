# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# TODO(GH#25151): decide on True behaviour
# # sort=True
idx = MultiIndex.from_product([[1, 0], ["a", "b"]])
other = idx[:0]
result = idx.union(other, sort=True)
expected = MultiIndex.from_product([[0, 1], ["a", "b"]])
tm.assert_index_equal(result, expected)
