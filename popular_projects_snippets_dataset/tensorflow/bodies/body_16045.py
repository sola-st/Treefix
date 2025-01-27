# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
row_splits = array_ops.constant([0, 2, 3, 5], dtype=dtypes.int64)
values = RowPartition.from_row_splits(row_splits)
nrows = values.nrows()
self.assertEqual(dtypes.int64, nrows.dtype)
