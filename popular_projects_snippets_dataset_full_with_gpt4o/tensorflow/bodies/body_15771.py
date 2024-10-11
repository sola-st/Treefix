# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths(lengths)
if num_row_partitions is not None:
    original = original._with_num_row_partitions(num_row_partitions)
expected = DynamicRaggedShape.from_lengths(expected_lengths)
actual = original[s]
self.assertShapeEq(expected, actual)
