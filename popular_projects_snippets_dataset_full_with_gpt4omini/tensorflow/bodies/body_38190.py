# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
# complex64
data = np.arange(1, 2, 0.10).reshape([5, 2]).astype(np.float32)
self._compareGradient(data)
self._compareBroadcastGradient(data)
# complex128
data = np.arange(1, 2, 0.10).reshape([5, 2]).astype(np.float64)
self._compareGradient(data)
