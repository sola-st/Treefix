# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
with self.cached_session():
    grid = _make_grid(dtype, grid_spec)
    actual = sm.log_cdf_laplace(grid).eval()

    # Basic tests.
    # isfinite checks for NaN and Inf.
    self.assertAllTrue(np.isfinite(actual))
    self.assertAllTrue((actual < 0))
    _check_strictly_increasing(actual)

    # Versus scipy.
    if not stats:
        exit()

    scipy_dist = stats.laplace(loc=0., scale=1.)
    expected = scipy_dist.logcdf(grid.astype(scipy_dtype))
    self.assertAllClose(
        expected.astype(np.float64),
        actual.astype(np.float64),
        rtol=error_spec.rtol,
        atol=error_spec.atol)
