# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
batch_size = 50
mu = self._rng.randn(batch_size)
sigma = self._rng.rand(batch_size) + 1.0
x = np.linspace(-8.0, 8.0, batch_size).astype(np.float64)

normal = normal_lib.Normal(loc=mu, scale=sigma)

sf = normal.survival_function(x)
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()), sf.get_shape())
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()),
    self.evaluate(sf).shape)
self.assertAllEqual(normal.batch_shape, sf.get_shape())
self.assertAllEqual(normal.batch_shape, self.evaluate(sf).shape)
if not stats:
    exit()
expected_sf = stats.norm(mu, sigma).sf(x)
self.assertAllClose(expected_sf, self.evaluate(sf), atol=0)
