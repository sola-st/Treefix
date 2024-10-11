# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
value = [0, 1, 2, 3, 4, 5]
shape = [2, 3]
expected = list(value)

self._testNDimConstantInitializer(value, shape, expected)
self._testNDimConstantInitializer(np.asarray(value), shape, expected)
self._testNDimConstantInitializer(
    np.asarray(value).reshape(tuple(shape)), shape, expected)
