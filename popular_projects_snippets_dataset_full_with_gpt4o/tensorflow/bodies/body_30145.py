# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
z = x[y]
self.tensorShapeEqual(z.get_shape(), tensor_shape.TensorShape([3, 7]))
