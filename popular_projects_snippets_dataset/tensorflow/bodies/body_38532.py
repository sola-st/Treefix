# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_unary_test.py
x = np.arange(-6 << 20, 6 << 20, 2 << 20).reshape(1, 3, 2).astype(np.int64)
self._compareCpu(x, np.square, math_ops.square)
self._compareBothSparse(x, np.square, math_ops.square)
