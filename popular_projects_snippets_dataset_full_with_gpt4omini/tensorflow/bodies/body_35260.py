# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
# Mu will be broadcast to [7, 7, 7].
mu = [7.]
sigma = [11., 12., 13.]

normal = normal_lib.Normal(loc=mu, scale=sigma)

self.assertAllEqual((3,), normal.mean().get_shape())
self.assertAllEqual([7., 7, 7], self.evaluate(normal.mean()))

self.assertAllEqual((3,), normal.mode().get_shape())
self.assertAllEqual([7., 7, 7], self.evaluate(normal.mode()))
