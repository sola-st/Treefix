# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = np.array([1., 2, 3])
b = np.array([2., 4, 1.2])
dist = beta_lib.Beta(a, b, allow_nan_stats=True)

expected_mode = (a - 1) / (a + b - 2)
expected_mode[0] = np.nan
self.assertEqual((3,), dist.mode().get_shape())
self.assertAllClose(expected_mode, self.evaluate(dist.mode()))

a = np.array([2., 2, 3])
b = np.array([1., 4, 1.2])
dist = beta_lib.Beta(a, b, allow_nan_stats=True)

expected_mode = (a - 1) / (a + b - 2)
expected_mode[0] = np.nan
self.assertEqual((3,), dist.mode().get_shape())
self.assertAllClose(expected_mode, self.evaluate(dist.mode()))
