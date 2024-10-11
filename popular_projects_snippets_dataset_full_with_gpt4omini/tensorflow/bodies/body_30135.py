# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
y = x[3:5, :, 4]
self.tensorShapeEqual(y.get_shape(), tensor_shape.TensorShape([2,
                                                               None]))
