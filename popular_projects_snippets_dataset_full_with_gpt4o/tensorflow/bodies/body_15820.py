# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
values = constant_op.constant([True, False, True, True, True])
rt_a = RaggedTensor.from_row_splits(values, [0, 3, 3, 5])
result = dynamic_ragged_shape.ragged_binary_elementwise_op_impl(
    gen_math_ops.logical_and, rt_a, rt_a)

expected_values = values
expected = RaggedTensor.from_row_splits(expected_values, [0, 3, 3, 5])

self.assertAllEqual(result, expected)
