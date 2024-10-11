# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
t_0 = ops.convert_to_tensor([0., 0., 0.])
self.assertEqual(dtypes.float32, t_0.dtype)

t_1 = ops.convert_to_tensor([0, 0, 0])
self.assertEqual(dtypes.int32, t_1.dtype)

t_2 = ops.convert_to_tensor([t_0, t_0, t_1], dtype=dtypes.float64)
self.assertEqual(dtypes.float64, t_2.dtype)
