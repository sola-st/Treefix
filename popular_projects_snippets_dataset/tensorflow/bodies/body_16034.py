# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
spec = RowPartitionSpec(nrows, nvals, uniform_row_length, dtype)
self.assertEqual(spec.nrows, expected_nrows)
self.assertEqual(spec.nvals, expected_nvals)
self.assertEqual(spec.uniform_row_length, expected_uniform_row_length)
self.assertEqual(spec.dtype, expected_dtype)
