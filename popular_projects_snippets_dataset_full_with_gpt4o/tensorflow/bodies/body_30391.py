# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
self._testAll(np.random.normal(0, 10, 210).reshape([2, 3, 5, 7]))
self._testAll(np.random.normal(0, 1e6, 210).reshape([2, 3, 5, 7]))
