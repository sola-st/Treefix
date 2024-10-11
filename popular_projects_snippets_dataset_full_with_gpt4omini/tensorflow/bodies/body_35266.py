# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
# sigma will be broadcast to [7, 7, 7]
mu = [1., 2., 3.]
sigma = [7.]

normal = normal_lib.Normal(loc=mu, scale=sigma)

self.assertAllEqual((3,), normal.stddev().get_shape())
self.assertAllEqual([7., 7, 7], self.evaluate(normal.stddev()))
