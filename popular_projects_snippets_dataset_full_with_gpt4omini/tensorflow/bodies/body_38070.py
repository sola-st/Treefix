# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
"""Assert all ops return the same shapes, and return 1st result."""
# Collect shapes and results for all ops, and assert static shapes match.
dynamic_indices_shape_ops = []
dynamic_values_shape_ops = []
static_indices_shape = None
static_values_shape = None
with self.cached_session() as sess:
    for op in ops:
        if static_indices_shape is None:
            static_indices_shape = op.indices.get_shape()
        else:
            self.assertAllEqual(
                static_indices_shape.as_list(), op.indices.get_shape().as_list())
        if static_values_shape is None:
            static_values_shape = op.values.get_shape()
        else:
            self.assertAllEqual(
                static_values_shape.as_list(), op.values.get_shape().as_list())
        dynamic_indices_shape_ops.append(array_ops.shape(op.indices))
        dynamic_values_shape_ops.append(array_ops.shape(op.values))
    results = sess.run(
        list(ops) + dynamic_indices_shape_ops + dynamic_values_shape_ops)
    op_count = len(ops)
    op_results = results[0:op_count]
    dynamic_indices_shapes = results[op_count:2 * op_count]
    dynamic_values_shapes = results[2 * op_count:3 * op_count]

# Assert static and dynamic tensor shapes, and result shapes, are all
# consistent.
static_indices_shape.assert_is_compatible_with(dynamic_indices_shapes[0])
static_values_shape.assert_is_compatible_with(dynamic_values_shapes[0])
self.assertAllEqual(dynamic_indices_shapes[0], op_results[0].indices.shape)
self.assertAllEqual(dynamic_values_shapes[0], op_results[0].values.shape)

# Assert dynamic shapes and values are the same for all ops.
for i in range(1, len(ops)):
    self.assertAllEqual(dynamic_indices_shapes[0], dynamic_indices_shapes[i])
    self.assertAllEqual(dynamic_values_shapes[0], dynamic_values_shapes[i])
    self.assertAllEqual(op_results[0].indices, op_results[i].indices)
    self.assertAllEqual(op_results[0].values, op_results[i].values)
    self.assertAllEqual(op_results[0].dense_shape, op_results[i].dense_shape)

exit(op_results[0])
