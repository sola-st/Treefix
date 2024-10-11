# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
value = [0, 1, 2, 3, 4, 5, 6, 7]
shape = [2, 3]
self._testNDimConstantInitializerMoreValues(value, shape)
self._testNDimConstantInitializerMoreValues(np.asarray(value), shape)
self._testNDimConstantInitializerMoreValues(
    np.asarray(value).reshape(tuple([2, 4])), shape)
