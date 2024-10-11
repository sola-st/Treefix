# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
self._compareCpu(
    np.arange(0, 8).reshape([2, 4]).astype(np.float32),
    np.array([1, 0]).astype(np.int32))
