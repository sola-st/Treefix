# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_reduce_op_test.py
rt_input = ragged_factory_ops.constant([[1, 2, 3], [4, 5]])
axis = array_ops.placeholder_with_default(constant_op.constant([0]), None)

if not context.executing_eagerly():
    self.assertRaisesRegex(ValueError,
                           r'axis must be known at graph construction time.',
                           ragged_math_ops.reduce_sum, rt_input, axis)
self.assertRaisesRegex(TypeError, r'axis must be an int; got str.*',
                       ragged_math_ops.reduce_sum, rt_input, ['x'])
