# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
err_msg = 'row_splits tensor may not be empty'
with self.assertRaisesRegex(ValueError, err_msg):
    RowPartition.from_row_splits([])
