# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# https://github.com/pandas-dev/pandas/issues/29896
# tests a corner case with get_indexer() with MultiIndexes where, when we
# need to "carry" across levels, proper tuple ordering is respected
#
# the MultiIndexes used in this test, visually, are:
# mult_idx_1:
#  0: 1 1 1 1
#  1:       2
#  2:     2 1
#  3:       2
#  4: 1 2 1 1
#  5:       2
#  6:     2 1
#  7:       2
#  8: 2 1 1 1
#  9:       2
# 10:     2 1
# 11:       2
# 12: 2 2 1 1
# 13:       2
# 14:     2 1
# 15:       2
#
# mult_idx_2:
#  0: 1 3 2 2
#  1: 2 3 2 2
mult_idx_1 = MultiIndex.from_product([[1, 2]] * 4)
mult_idx_2 = MultiIndex.from_tuples([(1, 3, 2, 2), (2, 3, 2, 2)])

# show the tuple orderings, which get_indexer() should respect
assert mult_idx_1[7] < mult_idx_2[0] < mult_idx_1[8]
assert mult_idx_1[-1] < mult_idx_2[1]

indexer = mult_idx_1.get_indexer(mult_idx_2)
expected = np.array([-1, -1], dtype=indexer.dtype)
tm.assert_almost_equal(expected, indexer)

backfill_indexer = mult_idx_1.get_indexer(mult_idx_2, method="bfill")
expected = np.array([8, -1], dtype=backfill_indexer.dtype)
tm.assert_almost_equal(expected, backfill_indexer)

pad_indexer = mult_idx_1.get_indexer(mult_idx_2, method="ffill")
expected = np.array([7, 15], dtype=pad_indexer.dtype)
tm.assert_almost_equal(expected, pad_indexer)
