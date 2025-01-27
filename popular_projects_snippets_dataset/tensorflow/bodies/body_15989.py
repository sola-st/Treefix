# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
value_rowids = constant_op.constant([0, 0, 2, 2, 2, 3, 4], dtypes.int64)
nrows = constant_op.constant(5, dtypes.int64)

rp = RowPartition.from_value_rowids(value_rowids, nrows, validate=False)

rp_value_rowids = rp.value_rowids()
rp_nrows = rp.nrows()
rp_row_splits = rp.row_splits()

self.assertIs(rp_value_rowids, value_rowids)  # value_rowids
self.assertIs(rp_nrows, nrows)  # nrows
self.assertAllEqual(rp_value_rowids, value_rowids)
self.assertAllEqual(rp_nrows, nrows)
self.assertAllEqual(rp_row_splits, [0, 2, 2, 5, 6, 7])
