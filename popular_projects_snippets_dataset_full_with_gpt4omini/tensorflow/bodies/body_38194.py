# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
data = np.arange(1, 2, 0.125).reshape([2, 4]).astype(np.float32)
self._compareMulGradient(data)
