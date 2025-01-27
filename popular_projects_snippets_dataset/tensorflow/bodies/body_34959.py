# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
raw_grid = _make_grid(dtype, grid_spec)
grid = ops.convert_to_tensor(raw_grid)
with self.cached_session():
    fn = sm.log_ndtr if self._use_log else sm.ndtr

    # If there are N points in the grid,
    # grad_eval.shape = (N, N), with grad_eval[i, j] the partial derivative of
    # the ith output point w.r.t. the jth grid point.  We only expect the
    # diagonal to be nonzero.
    # TODO(b/31131137): Replace tf.compat.v1.test.compute_gradient with our
    # own custom gradient evaluation to ensure we correctly handle small
    # function delta.
    grad_eval, _ = gradient_checker.compute_gradient(grid, grid_spec.shape,
                                                     fn(grid),
                                                     grid_spec.shape)
    grad_eval = np.diag(grad_eval)

    # Check for NaN separately in order to get informative failures.
    self.assert_all_false(np.isnan(grad_eval))
    self.assert_all_true(grad_eval > 0.)
    # isfinite checks for NaN and Inf.
    self.assert_all_true(np.isfinite(grad_eval))

    # Do the same checks but explicitly compute the gradient.
    # (We did this because we're not sure if we trust
    # tf.test.compute_gradient.)
    grad_eval = gradients_impl.gradients(fn(grid), grid)[0].eval()
    self.assert_all_false(np.isnan(grad_eval))
    if self._use_log:
        g = np.reshape(grad_eval, [-1])
        half = np.ceil(len(g) / 2)
        self.assert_all_true(g[:int(half)] > 0.)
        self.assert_all_true(g[int(half):] >= 0.)
    else:
        # The ndtr gradient will only be non-zero in the range [-14, 14] for
        # float32 and [-38, 38] for float64.
        self.assert_all_true(grad_eval >= 0.)
    # isfinite checks for NaN and Inf.
    self.assert_all_true(np.isfinite(grad_eval))

    # Versus scipy.
    if not (special and stats):
        exit()

    expected = stats.norm.pdf(raw_grid)
    if self._use_log:
        expected /= special.ndtr(raw_grid)
        expected[np.isnan(expected)] = 0.
    # Scipy prematurely goes to zero at some places that we don't.  So don't
    # include these in the comparison.
    self.assertAllClose(
        expected.astype(np.float64)[expected < 0],
        grad_eval.astype(np.float64)[expected < 0],
        rtol=error_spec.rtol,
        atol=error_spec.atol)
