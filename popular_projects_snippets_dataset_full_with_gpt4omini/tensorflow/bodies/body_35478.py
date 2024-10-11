# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
"""Zero isn't in the support of the gamma distribution.

    But quantized floating point math has its limits.
    TODO(bjp): Implement log-gamma sampler for small-shape distributions.

    Args:
      alpha: float shape value to test
    """
try:
    from scipy import stats  # pylint: disable=g-import-not-at-top
except ImportError as e:
    tf_logging.warn("Cannot test zero density proportions: %s" % e)
    exit()
allowable_zeros = {
    dtypes.float16: stats.gamma(alpha).cdf(np.finfo(np.float16).tiny),
    dtypes.float32: stats.gamma(alpha).cdf(np.finfo(np.float32).tiny),
    dtypes.float64: stats.gamma(alpha).cdf(np.finfo(np.float64).tiny)
}
failures = []
for dt in dtypes.float16, dtypes.float32, dtypes.float64:
    sampler = self._Sampler(10000, alpha, 1.0, dt, seed=12345)
    x = sampler()
    allowable = allowable_zeros[dt] * x.size
    allowable = allowable * 2 if allowable < 10 else allowable * 1.05
    if np.sum(x <= 0) > allowable:
        failures += [dt]
self.assertEqual([], failures)
