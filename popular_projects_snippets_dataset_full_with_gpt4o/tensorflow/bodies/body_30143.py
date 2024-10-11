# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
y = x[::-1, :, array_ops.newaxis, ::-2]
self.tensorShapeEqual(y.get_shape(),
                      tensor_shape.TensorShape([5, None, 1, 4]))
