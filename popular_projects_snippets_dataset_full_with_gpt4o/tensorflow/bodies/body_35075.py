# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x = constant_op.constant(1.)
shape = du.prefer_static_shape(x)
self.assertIsInstance(shape, np.ndarray)
self.assertAllEqual(np.array([]), shape)
