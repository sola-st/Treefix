# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
# Scipy.stats.norm cannot deal with the shapes in the other test.
mu_v = 2.34
sigma_v = 4.56
normal = normal_lib.Normal(loc=mu_v, scale=sigma_v)

entropy = normal.entropy()
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()), entropy.get_shape())
self.assertAllEqual(
    self.evaluate(normal.batch_shape_tensor()),
    self.evaluate(entropy).shape)
self.assertAllEqual(normal.batch_shape, entropy.get_shape())
self.assertAllEqual(normal.batch_shape, self.evaluate(entropy).shape)
# scipy.stats.norm cannot deal with these shapes.
if not stats:
    exit()
expected_entropy = stats.norm(mu_v, sigma_v).entropy()
self.assertAllClose(expected_entropy, self.evaluate(entropy))
