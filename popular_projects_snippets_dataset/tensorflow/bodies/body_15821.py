# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()

rt_a = ragged_factory_ops.constant([[3, 1, 3], [3]])
b = constant_op.constant(3)
rt_expected = ragged_factory_ops.constant([[True, False, True], [True]])

result = dynamic_ragged_shape.ragged_binary_elementwise_op_impl(
    math_ops.equal, rt_a, b)
self.assertAllEqual(result, rt_expected)
