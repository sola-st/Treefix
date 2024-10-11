# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
raw_rt = [[[[7, 4], [5, 6]], [[1, 2], [3, 7]]], [[[7, 4], [5, 6]]],
          [[[1, 2], [3, 7]]]]
raw_rt = ragged_factory_ops.constant_value(raw_rt)
actual_shape = DynamicRaggedShape.from_tensor(raw_rt)
expected_shape = DynamicRaggedShape.from_lengths(
    [3, (2, 1, 1), 2, 2])._with_num_row_partitions(3)
self.assertShapeEq(actual_shape, expected_shape)
