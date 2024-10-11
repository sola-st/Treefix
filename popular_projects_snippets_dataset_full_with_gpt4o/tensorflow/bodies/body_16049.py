# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
with self.assertRaisesRegex(error_type, error_regex):
    a._merge_with(b)
