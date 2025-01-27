# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
value = [0, 1, 2, 3, 4, 5]
shape = [2, 4]
expected = list(value)

self._testNDimConstantInitializerLessValues("list", value, shape, expected)
self._testNDimConstantInitializerLessValues("ndarray", np.asarray(value),
                                            shape, expected)
self._testNDimConstantInitializerLessValues(
    "2D-ndarray",
    np.asarray(value).reshape(tuple([2, 3])), shape, expected)
