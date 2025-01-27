# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
y = x[:2:3, :, array_ops.newaxis, 50:3,]
self.tensorShapeEqual(y.get_shape(),
                      tensor_shape.TensorShape([1, None, 1, 0]))
