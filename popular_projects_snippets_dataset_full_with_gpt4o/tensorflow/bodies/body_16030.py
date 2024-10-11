# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = RowPartition.from_row_splits([0, 3, 4, 5])
static_nrows = rp.static_nrows
self.assertIsInstance(static_nrows, int)
self.assertAllEqual(3, static_nrows)
