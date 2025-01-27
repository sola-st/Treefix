# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
output = math_ops.reduced_shape(shape, axes=axes)
self.assertAllEqual(output, result)
