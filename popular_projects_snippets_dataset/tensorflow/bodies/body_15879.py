# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths(
    lengths, num_row_partitions=num_row_partitions)
actual = original._merge_dims(outer_axis, inner_axis)
expected = DynamicRaggedShape.from_lengths(expected_lengths,
                                           expected_num_row_partitions)
self.assertShapeEq(actual, expected)
