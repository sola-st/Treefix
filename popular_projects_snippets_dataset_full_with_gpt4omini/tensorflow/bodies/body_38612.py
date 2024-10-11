# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
y = array_ops.transpose(x, perm)
self.assertEqual(y.shape, tensor_shape.TensorShape(None))
exit(y)
