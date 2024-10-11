# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
value = [0, 1, 2, 3, 4, 5]
shape = [2, 3]
expected = list(value)

self._testNDimConstantInitializer("list", value, shape, expected)
self._testNDimConstantInitializer("ndarray", np.asarray(value), shape,
                                  expected)
self._testNDimConstantInitializer("2D-ndarray",
                                  np.asarray(value).reshape(tuple(shape)),
                                  shape, expected)
