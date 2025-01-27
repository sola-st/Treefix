# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
"""Compare to the explicit reparameterization derivative.

    Verifies that the computed derivative satisfies
    dsample / dalpha = d igammainv(alpha, u) / dalpha,
    where u = igamma(alpha, sample).

    Args:
      dtype: TensorFlow dtype to perform the computations in.
    """
delta = 1e-3
np_dtype = dtype.as_numpy_dtype
try:
    from scipy import misc  # pylint: disable=g-import-not-at-top
    from scipy import special  # pylint: disable=g-import-not-at-top

    alpha_val = np.logspace(-2, 3, dtype=np_dtype)
    alpha = constant_op.constant(alpha_val)
    sample = random_ops.random_gamma(
        [], alpha, np_dtype(1.0), dtype=dtype, seed=12345)
    actual = gradients_impl.gradients(sample, alpha)[0]

    (sample_val, actual_val) = self.evaluate((sample, actual))

    u = special.gammainc(alpha_val, sample_val)
    expected_val = misc.derivative(
        lambda alpha_prime: special.gammaincinv(alpha_prime, u),
        alpha_val, dx=delta * alpha_val)

    self.assertAllClose(actual_val, expected_val, rtol=1e-3, atol=1e-3)
except ImportError as e:
    tf_logging.warn("Cannot use special functions in a test: %s" % str(e))
