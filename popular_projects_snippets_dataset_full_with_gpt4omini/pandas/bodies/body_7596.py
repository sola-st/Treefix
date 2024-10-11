# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# https://github.com/pandas-dev/pandas/issues/29896
# test getting an indexer for another index with different methods
# confirms that getting an indexer without a filling method, getting an
# indexer and backfilling, and getting an indexer and padding all behave
# correctly in the case where all of the target values fall in between
# several levels in the MultiIndex into which they are getting an indexer
#
# visually, the MultiIndexes used in this test are:
# mult_idx_1:
#  0: -1 0
#  1:    2
#  2:    3
#  3:    4
#  4:  0 0
#  5:    2
#  6:    3
#  7:    4
#  8:  1 0
#  9:    2
# 10:    3
# 11:    4
#
# mult_idx_2:
#  0: 0 1
#  1:   3
#  2:   4
mult_idx_1 = MultiIndex.from_product([[-1, 0, 1], [0, 2, 3, 4]])
mult_idx_2 = MultiIndex.from_product([[0], [1, 3, 4]])

indexer = mult_idx_1.get_indexer(mult_idx_2)
expected = np.array([-1, 6, 7], dtype=indexer.dtype)
tm.assert_almost_equal(expected, indexer)

backfill_indexer = mult_idx_1.get_indexer(mult_idx_2, method="backfill")
expected = np.array([5, 6, 7], dtype=backfill_indexer.dtype)
tm.assert_almost_equal(expected, backfill_indexer)

# ensure the legacy "bfill" option functions identically to "backfill"
backfill_indexer = mult_idx_1.get_indexer(mult_idx_2, method="bfill")
expected = np.array([5, 6, 7], dtype=backfill_indexer.dtype)
tm.assert_almost_equal(expected, backfill_indexer)

pad_indexer = mult_idx_1.get_indexer(mult_idx_2, method="pad")
expected = np.array([4, 6, 7], dtype=pad_indexer.dtype)
tm.assert_almost_equal(expected, pad_indexer)

# ensure the legacy "ffill" option functions identically to "pad"
pad_indexer = mult_idx_1.get_indexer(mult_idx_2, method="ffill")
expected = np.array([4, 6, 7], dtype=pad_indexer.dtype)
tm.assert_almost_equal(expected, pad_indexer)
