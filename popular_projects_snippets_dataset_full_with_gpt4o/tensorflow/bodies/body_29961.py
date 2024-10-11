# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
self._testAll(
    (1 + 2j) * np.arange(-15, 15).reshape([2, 3, 5]).astype(np.complex64))
self._testAll(
    (1 + 2j) *
    np.random.normal(size=30).reshape([2, 3, 5]).astype(np.complex64))
self._testAll(np.empty((2, 0, 5)).astype(np.complex64))
