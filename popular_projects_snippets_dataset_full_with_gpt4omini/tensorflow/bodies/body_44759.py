# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensors_test.py
self.assertTrue(tensors.is_range_tensor(math_ops.range(1)))
self.assertTrue(tensors.is_range_tensor(math_ops.range(1, 2)))
self.assertTrue(tensors.is_range_tensor(math_ops.range(1, 2, 3)))
self.assertFalse(tensors.is_range_tensor(None))
self.assertFalse(tensors.is_range_tensor(constant_op.constant(range(1))))
