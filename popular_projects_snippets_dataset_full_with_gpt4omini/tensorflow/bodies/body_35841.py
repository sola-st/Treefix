# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
p = state_ops.variable_op([1, 2], dtypes.float32)
self.assertEqual([1, 2], p.get_shape())
p = state_ops.variable_op([1, 2], dtypes.float32, set_shape=False)
self.assertEqual(tensor_shape.unknown_shape(), p.get_shape())
