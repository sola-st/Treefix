# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
self._testBoth(np.array(1 + 2j).astype(np.complex64))
self._testBoth((1 + 2j) * np.arange(0, 21).astype(np.complex64))
self._testBoth(
    (1 + 2j) * np.arange(0, 21).reshape([3, 7]).astype(np.complex64))
self._testBoth(
    (1 + 2j) * np.arange(0, 210).reshape([2, 3, 5, 7]).astype(np.complex64))
self._testBoth(
    (1 + 2j) *
    np.arange(0, 1260).reshape([2, 3, 5, 7, 2, 3]).astype(np.complex64))
