# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = RowPartition.from_row_splits(rs)
static_nrows = rp.static_nrows
self.assertIsNone(static_nrows)
