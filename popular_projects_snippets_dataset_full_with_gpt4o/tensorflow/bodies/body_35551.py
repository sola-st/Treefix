# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
"""Compare to the implicit reparameterization derivative.

    Let's derive the formula we compare to.

    Start from the fact that CDF maps a random variable to the Uniform
    random variable:
      igamma(alpha, sample) = u, where u ~ Uniform(0, 1).

    Apply d / dalpha to both sides:
      d igamma(alpha, sample) / dalpha
          + d igamma(alpha, sample) / dsample * dsample/dalpha  = 0
      d igamma(alpha, sample) / dalpha
          + d igamma(alpha, sample) / dsample * dsample / dalpha = 0
      dsample/dalpha = - (d igamma(alpha, sample) / dalpha)
                        / d igamma(alpha, sample) / dsample

    This is the equation (8) of https://arxiv.org/abs/1805.08498

    Args:
      dtype: TensorFlow dtype to perform the computations in.
    """
np_dtype = dtype.as_numpy_dtype
alpha = constant_op.constant(np.logspace(-2, 3, dtype=np_dtype))
sample = random_ops.random_gamma(
    [], alpha, np_dtype(1.0), dtype=dtype, seed=12345)
actual = gradients_impl.gradients(sample, alpha)[0]

sample_sg = array_ops.stop_gradient(sample)
cdf = math_ops.igamma(alpha, sample_sg)
dcdf_dalpha, dcdf_dsample = gradients_impl.gradients(
    cdf, [alpha, sample_sg])
# Numerically unstable due to division, do not try at home.
expected = -dcdf_dalpha / dcdf_dsample

(actual_val, expected_val) = self.evaluate((actual, expected))

self.assertAllClose(actual_val, expected_val, rtol=1e-3, atol=1e-3)
