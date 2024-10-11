# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = array_ops.zeros((2, 3, 4))
shape = du.prefer_static_shape(x)
self.assertIsInstance(shape, np.ndarray)
self.assertAllEqual(np.array([2, 3, 4]), shape)
