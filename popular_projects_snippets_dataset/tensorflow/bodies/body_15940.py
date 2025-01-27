# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(error_type, error_regex):
    spec._with_num_row_partitions(num_row_partitions)
