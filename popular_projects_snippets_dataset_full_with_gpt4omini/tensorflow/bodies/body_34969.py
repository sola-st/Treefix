# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
with self.cached_session() as sess:
    # On the lower branch, log_cdf_laplace(x) = x, so we know this will be
    # fine, but test to -200 anyways.
    grid = _make_grid(
        np.float64, GridSpec(min=-200, max=700, shape=[20, 100]))
    grid = ops.convert_to_tensor(grid)

    actual = sm.log_cdf_laplace(grid)
    grad = gradients_impl.gradients(actual, grid)[0]

    actual_, grad_ = self.evaluate([actual, grad])

    # isfinite checks for NaN and Inf.
    self.assertAllTrue(np.isfinite(actual_))
    self.assertAllTrue(np.isfinite(grad_))
    self.assertFalse(np.any(actual_ == 0))
    self.assertFalse(np.any(grad_ == 0))
