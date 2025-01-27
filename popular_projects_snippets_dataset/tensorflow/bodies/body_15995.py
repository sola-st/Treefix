# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
row_limits = constant_op.constant([2, 2, 5, 6, 7], dtypes.int64)

rp = RowPartition.from_row_limits(row_limits, validate=False)
self.assertEqual(rp.dtype, dtypes.int64)

rp_row_limits = rp.row_limits()
rp_row_splits = rp.row_splits()
rp_nrows = rp.nrows()

self.assertAllEqual(rp_nrows, 5)
self.assertAllEqual(rp_row_limits, row_limits)
self.assertAllEqual(rp_row_splits, [0, 2, 2, 5, 6, 7])
