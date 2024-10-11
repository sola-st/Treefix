# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
row_splits = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)

rp = RowPartition.from_row_splits(row_splits, validate=False)
self.assertEqual(rp.dtype, dtypes.int64)

rp_row_splits = rp.row_splits()
rp_nrows = rp.nrows()

self.assertIs(rp_row_splits, row_splits)
self.assertAllEqual(rp_nrows, 5)
