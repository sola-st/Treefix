# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/reshape_op_test.py
x = np.arange(1., 7.).reshape([1, 6]).astype(np.complex64)
self._testBothReshape(x, [2, 3])
