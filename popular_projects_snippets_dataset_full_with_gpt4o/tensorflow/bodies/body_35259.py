# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
mu_v = np.array([1.0, 1.0, 1.0])
sigma_v = np.array([[1.0, 2.0, 3.0]]).T
normal = normal_lib.Normal(loc=mu_v, scale=sigma_v)

# scipy.stats.norm cannot deal with these shapes.
sigma_broadcast = mu_v * sigma_v
expected_entropy = 0.5 * np.log(2 * np.pi * np.exp(1) * sigma_broadcast**2)
entropy = normal.entropy()
np.testing.assert_allclose(expected_entropy, self.evaluate(entropy))
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()), entropy.get_shape())
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()),
    self.evaluate(entropy).shape)
self.assertAllEqual(normal.batch_shape, entropy.get_shape())
self.assertAllEqual(normal.batch_shape, self.evaluate(entropy).shape)
