# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
batch_size = 50
mu = self._rng.randn(batch_size)
sigma = self._rng.rand(batch_size) + 1.0
x = np.linspace(-100.0, 10.0, batch_size).astype(np.float64)

normal = normal_lib.Normal(loc=mu, scale=sigma)

cdf = normal.log_cdf(x)
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()), cdf.get_shape())
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()),
    self.evaluate(cdf).shape)
self.assertAllEqual(normal.batch_shape, cdf.get_shape())
self.assertAllEqual(normal.batch_shape, self.evaluate(cdf).shape)

if not stats:
    exit()
expected_cdf = stats.norm(mu, sigma).logcdf(x)
self.assertAllClose(expected_cdf, self.evaluate(cdf), atol=0, rtol=1e-3)
