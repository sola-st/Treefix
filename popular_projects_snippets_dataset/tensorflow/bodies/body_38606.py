# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
self._testBoth(np.arange(0, 21).reshape([3, 7]).astype(np.int32))
self._testBoth(np.arange(0, 210).reshape([2, 3, 5, 7]).astype(np.int32))
self._testBoth(
    np.arange(0, 1260).reshape([2, 3, 5, 7, 2, 3]).astype(np.int32))
