# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
x = np.arange(40, 40 + 6).reshape(6).astype(np.float32)
self._compareBoth(x, np.tanh, math_ops.tanh)
x = np.arange(-40, -40 + 6).reshape(6).astype(np.float32)
self._compareBoth(x, np.tanh, math_ops.tanh)
