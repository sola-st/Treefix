# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
x = np.arange(6).reshape(1, 3, 2).astype(np.uint8)
self._compareBoth(x, np.square, math_ops.square)
