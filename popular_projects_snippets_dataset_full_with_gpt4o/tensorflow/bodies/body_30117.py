# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
t = constant_op.constant([1, 2, 3])
d = tensor_shape.Dimension(None)
self.assertAllEqual(t[d:d:d], t)
