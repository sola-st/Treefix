# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_setops.py
# TODO(GH#25151): decide on True behaviour
# sort=True
idx = Index([1, 0, 2])
# default, sort=None
other = idx[slice_]

result = idx.union(other, sort=True)
expected = Index([0, 1, 2])
tm.assert_index_equal(result, expected)
