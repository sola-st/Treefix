# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_index_equal.py
idx1 = Index([0, 1, 2])
idx2 = RangeIndex(3)

tm.assert_index_equal(idx1, idx2, exact=exact)
