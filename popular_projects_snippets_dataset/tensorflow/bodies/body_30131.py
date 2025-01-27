# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
y = x[...]
self.assertAllEqual(y.get_shape().ndims, None)
