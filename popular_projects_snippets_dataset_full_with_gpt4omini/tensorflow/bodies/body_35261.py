# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
batch_size = 52
mu = self._rng.randn(batch_size)
sigma = self._rng.rand(batch_size) + 1.0
p = np.linspace(0., 1.0, batch_size - 2).astype(np.float64)
# Quantile performs piecewise rational approximation so adding some
# special input values to make sure we hit all the pieces.
p = np.hstack((p, np.exp(-33), 1. - np.exp(-33)))

normal = normal_lib.Normal(loc=mu, scale=sigma)
x = normal.quantile(p)

self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()), x.get_shape())
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()),
    self.evaluate(x).shape)
self.assertAllEqual(normal.batch_shape, x.get_shape())
self.assertAllEqual(normal.batch_shape, self.evaluate(x).shape)

if not stats:
    exit()
expected_x = stats.norm(mu, sigma).ppf(p)
self.assertAllClose(expected_x, self.evaluate(x), atol=0.)
