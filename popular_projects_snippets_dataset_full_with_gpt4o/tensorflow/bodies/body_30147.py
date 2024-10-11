# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
z = x[y, ::-2]
self.tensorShapeEqual(z.get_shape(), tensor_shape.TensorShape([2, 7]))
