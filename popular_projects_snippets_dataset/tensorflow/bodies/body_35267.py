# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
mu = constant_op.constant(3.0)
sigma = constant_op.constant(math.sqrt(3.0))
mu_v = 3.0
sigma_v = np.sqrt(3.0)
n = constant_op.constant(100000)
normal = normal_lib.Normal(loc=mu, scale=sigma)
samples = normal.sample(n)
sample_values = self.evaluate(samples)
# Note that the standard error for the sample mean is ~ sigma / sqrt(n).
# The sample variance similarly is dependent on sigma and n.
# Thus, the tolerances below are very sensitive to number of samples
# as well as the variances chosen.
self.assertEqual(sample_values.shape, (100000,))
self.assertAllClose(sample_values.mean(), mu_v, atol=1e-1)
self.assertAllClose(sample_values.std(), sigma_v, atol=1e-1)

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
