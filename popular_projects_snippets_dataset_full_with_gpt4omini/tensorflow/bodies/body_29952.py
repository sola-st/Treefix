# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
t_0 = ops.convert_to_tensor([[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]])
self.assertEqual(dtypes.float32, t_0.dtype)

t_1 = ops.convert_to_tensor([[0., 0., 0.], constant_op.constant(
    [0., 0., 0.], dtype=dtypes.float64), [0., 0., 0.]])
self.assertEqual(dtypes.float64, t_1.dtype)

t_2 = ops.convert_to_tensor(
    [[0., 0., 0.], [0., 0., 0.], [0., 0., 0.]], dtype=dtypes.float64)
self.assertEqual(dtypes.float64, t_2.dtype)

t_3 = ops.convert_to_tensor(
    [[0., 0., 0.],
     constant_op.constant([0., 0., 0.], dtype=dtypes.float64), [0., 0., 0.]
    ],
    dtype=dtypes.float32)
self.assertEqual(dtypes.float32, t_3.dtype)

t_4 = ops.convert_to_tensor(
    [constant_op.constant([0., 0., 0.], dtype=dtypes.float64)],
    dtype=dtypes.float32)
self.assertEqual(dtypes.float32, t_4.dtype)

with self.assertRaises(TypeError):
    ops.convert_to_tensor([
        constant_op.constant(
            [0., 0., 0.], dtype=dtypes.float32), constant_op.constant(
                [0., 0., 0.], dtype=dtypes.float64), [0., 0., 0.]
    ])
