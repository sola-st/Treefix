# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
spec = RowPartitionSpec()
self.assertIsNone(spec.nrows)
self.assertIsNone(spec.nvals)
self.assertIsNone(spec.uniform_row_length)
self.assertEqual(spec.dtype, dtypes.int64)
