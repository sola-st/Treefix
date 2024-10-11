# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
# nrows is known at graph creation time.
value_rowids = constant_op.constant([0, 0, 2, 2, 2, 3, 4], dtypes.int64)
# TODO(martinz): add nrows
rp = RowPartition.from_value_rowids(value_rowids, validate=False)
self.assertEqual(rp.dtype, dtypes.int64)

rp_row_splits = rp.row_splits()
rp_value_rowids = rp.value_rowids()
rp_nrows = rp.nrows()

self.assertIs(rp_value_rowids, value_rowids)  # value_rowids
self.assertAllEqual(rp_value_rowids, value_rowids)
self.assertAllEqual(rp_nrows, 5)
self.assertAllEqual(rp_row_splits, [0, 2, 2, 5, 6, 7])
