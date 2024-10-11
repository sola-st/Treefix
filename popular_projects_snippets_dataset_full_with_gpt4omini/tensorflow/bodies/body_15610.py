# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_range_op_test.py
self.assertAllEqual(
    ragged_math_ops.range(0, 0, 1).shape.as_list(), [1, None])
self.assertAllEqual(
    ragged_math_ops.range([1, 2, 3]).shape.as_list(), [3, None])
self.assertAllEqual(
    ragged_math_ops.range([1, 2, 3], [4, 5, 6]).shape.as_list(), [3, None])
