# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
x = constant_op.constant([[1, 2], [3, 4]])
out = math_ops.matmul(v, x)
self.assertEqual(out.shape, tensor_shape.TensorShape([2, 2]))
