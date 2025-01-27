# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
batch_size = 2
mu = constant_op.constant([[3.0, -3.0]] * batch_size)
sigma = constant_op.constant(
    [[math.sqrt(2.0), math.sqrt(3.0)]] * batch_size)
mu_v = [3.0, -3.0]
sigma_v = [np.sqrt(2.0), np.sqrt(3.0)]
n = constant_op.constant(100000)
normal = normal_lib.Normal(loc=mu, scale=sigma)
samples = normal.sample(n)
sample_values = self.evaluate(samples)
# Note that the standard error for the sample mean is ~ sigma / sqrt(n).
# The sample variance similarly is dependent on sigma and n.
# Thus, the tolerances below are very sensitive to number of samples
# as well as the variances chosen.
self.assertEqual(samples.get_shape(), (100000, batch_size, 2))
self.assertAllClose(sample_values[:, 0, 0].mean(), mu_v[0], atol=1e-1)
self.assertAllClose(sample_values[:, 0, 0].std(), sigma_v[0], atol=1e-1)
self.assertAllClose(sample_values[:, 0, 1].mean(), mu_v[1], atol=1e-1)
self.assertAllClose(sample_values[:, 0, 1].std(), sigma_v[1], atol=1e-1)

expected_samples_shape = tensor_shape.TensorShape(
    [self.evaluate(n)]).concatenate(
        tensor_shape.TensorShape(
            self.evaluate(normal.batch_shape_tensor())))
self.assertAllEqual(expected_samples_shape, samples.get_shape())
self.assertAllEqual(expected_samples_shape, sample_values.shape)

expected_samples_shape = (
    tensor_shape.TensorShape([self.evaluate(n)]).concatenate(
        normal.batch_shape))
self.assertAllEqual(expected_samples_shape, samples.get_shape())
self.assertAllEqual(expected_samples_shape, sample_values.shape)
