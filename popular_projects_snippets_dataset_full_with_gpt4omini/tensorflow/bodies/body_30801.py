# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/betainc_op_test.py
with self.cached_session() as sess:
    space = np.logspace(-8, 5).tolist()
    space_x = np.linspace(1e-16, 1 - 1e-16).tolist()
    ga_s, gb_s, gx_s = zip(*list(itertools.product(space, space, space_x)))
    # Test grads are never nan
    ga_s_t = constant_op.constant(ga_s, dtype=dtypes.float32)
    gb_s_t = constant_op.constant(gb_s, dtype=dtypes.float32)
    gx_s_t = constant_op.constant(gx_s, dtype=dtypes.float32)
    tf_gout_t = math_ops.betainc(ga_s_t, gb_s_t, gx_s_t)
    tf_gout, grads_x = sess.run(
        [tf_gout_t,
         gradients_impl.gradients(tf_gout_t, [ga_s_t, gb_s_t, gx_s_t])[2]])

    # Equivalent to `assertAllFalse` (if it existed).
    self.assertAllEqual(
        np.zeros_like(grads_x).astype(np.bool_), np.isnan(tf_gout))
    self.assertAllEqual(
        np.zeros_like(grads_x).astype(np.bool_), np.isnan(grads_x))
