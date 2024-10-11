# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = np.array([1.1, 2, 3])
b = np.array([2., 4, 1.2])
expected_mode = (a - 1) / (a + b - 2)
dist = beta_lib.Beta(a, b)
self.assertEqual(dist.mode().get_shape(), (3,))
self.assertAllClose(expected_mode, self.evaluate(dist.mode()))
