# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
nvals = constant_op.constant(7)
row_starts = constant_op.constant([0, 2, 2, 5, 6], dtypes.int64)

rp = RowPartition.from_row_starts(row_starts, nvals, validate=False)
self.assertEqual(rp.dtype, dtypes.int64)

rp_row_starts = rp.row_starts()
rp_row_splits = rp.row_splits()
rp_nrows = rp.nrows()

self.assertAllEqual(rp_nrows, 5)
self.assertAllEqual(rp_row_starts, row_starts)
self.assertAllEqual(rp_row_splits, [0, 2, 2, 5, 6, 7])
