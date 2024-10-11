# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
n = 5
samples = self.prng.uniform(size=(10000, n + 1))
samples[:, -1] = np.nan  # Force use of our own algorithm.

variance_0 = nanops.nanvar(samples, axis=1, skipna=True, ddof=0).mean()
variance_1 = nanops.nanvar(samples, axis=1, skipna=True, ddof=1).mean()
variance_2 = nanops.nanvar(samples, axis=1, skipna=True, ddof=2).mean()

# The unbiased estimate.
var = 1.0 / 12
tm.assert_almost_equal(variance_1, var, rtol=1e-2)

# The underestimated variance.
tm.assert_almost_equal(variance_0, (n - 1.0) / n * var, rtol=1e-2)

# The overestimated variance.
tm.assert_almost_equal(variance_2, (n - 1.0) / (n - 2.0) * var, rtol=1e-2)
