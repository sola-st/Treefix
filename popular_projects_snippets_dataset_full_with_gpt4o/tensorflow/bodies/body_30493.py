# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
self._testEmpty(dtype)
self._testBatch(dtype)
if dtype != np.complex64:
    self._testDefaultValuesBatch(dtype)
self._testValueTypeBatch(dtype)
