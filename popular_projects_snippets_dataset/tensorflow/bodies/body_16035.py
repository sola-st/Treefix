# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
with self.assertRaisesRegex(ValueError, error):
    RowPartitionSpec(nrows, nvals, uniform_row_length, dtype)
