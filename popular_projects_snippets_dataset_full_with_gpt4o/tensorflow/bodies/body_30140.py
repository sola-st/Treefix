# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
y = x[1:5:2, :, array_ops.newaxis, 50:3,]
self.tensorShapeEqual(y.get_shape(),
                      tensor_shape.TensorShape([2, None, 1, 0]))
