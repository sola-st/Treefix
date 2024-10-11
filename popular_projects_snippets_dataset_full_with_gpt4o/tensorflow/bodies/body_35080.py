# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = constant_op.constant([])
value = du.prefer_static_value(x)
self.assertIsInstance(value, np.ndarray)
self.assertAllEqual(np.array([]), value)
