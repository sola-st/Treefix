# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/beta_test.py
a = [[1., 2, 3]]
b = [[2., 4, 3]]
dist = beta_lib.Beta(a, b)
self.assertEqual([1, 3], dist.concentration1.get_shape())
self.assertAllClose(a, self.evaluate(dist.concentration1))
