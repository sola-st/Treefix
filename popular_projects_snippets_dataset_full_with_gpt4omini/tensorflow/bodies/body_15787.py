# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape = DynamicRaggedShape.from_lengths(lengths)._with_num_row_partitions(
    num_row_partitions)
with self.assertRaisesRegex(error_type, error_regex):
    shape.is_uniform(axis)
