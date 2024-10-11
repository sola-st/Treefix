# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = array_ops.zeros((2, 3, 4))
value = du.prefer_static_value(x)
self.assertIsInstance(value, np.ndarray)
self.assertAllEqual(np.zeros((2, 3, 4)), value)
