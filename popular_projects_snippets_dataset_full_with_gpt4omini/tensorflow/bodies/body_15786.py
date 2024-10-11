# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape = DynamicRaggedShape.from_lengths(lengths)._with_num_row_partitions(
    num_row_partitions)
actual = shape.is_uniform(axis)
self.assertFalse(actual)
