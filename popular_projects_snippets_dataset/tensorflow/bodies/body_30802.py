# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/betainc_op_test.py
err_tolerance = 1e-3
with self.cached_session():
    # Test gradient
    ga_s = np.abs(np.random.randn(2, 2) * 30)  # in (0, infty)
    gb_s = np.abs(np.random.randn(2, 2) * 30)  # in (0, infty)
    gx_s = np.random.rand(2, 2)  # in (0, 1)
    tf_ga_s = constant_op.constant(ga_s, dtype=dtypes.float64)
    tf_gb_s = constant_op.constant(gb_s, dtype=dtypes.float64)
    tf_gx_s = constant_op.constant(gx_s, dtype=dtypes.float64)
    tf_gout_t = math_ops.betainc(tf_ga_s, tf_gb_s, tf_gx_s)
    err = gradient_checker.compute_gradient_error(
        [tf_gx_s], [gx_s.shape], tf_gout_t, gx_s.shape)
    tf_logging.info("betainc gradient err = %g " % err)
    self.assertLess(err, err_tolerance)

    # Test broadcast gradient
    gx_s = np.random.rand()  # in (0, 1)
    tf_gx_s = constant_op.constant(gx_s, dtype=dtypes.float64)
    tf_gout_t = math_ops.betainc(tf_ga_s, tf_gb_s, tf_gx_s)
    err = gradient_checker.compute_gradient_error(
        [tf_gx_s], [()], tf_gout_t, ga_s.shape)
    tf_logging.info("betainc gradient err = %g " % err)
    self.assertLess(err, err_tolerance)
