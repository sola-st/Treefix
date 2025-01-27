# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
row_lengths = constant_op.constant([2, 0, 3, 1, 1], dtypes.int64)

rp = RowPartition.from_row_lengths(row_lengths, validate=False)
self.assertEqual(rp.dtype, dtypes.int64)

rp_row_lengths = rp.row_lengths()
rp_nrows = rp.nrows()

self.assertIs(rp_row_lengths, row_lengths)  # nrows
self.assertAllEqual(rp_nrows, 5)
self.assertAllEqual(rp_row_lengths, row_lengths)
