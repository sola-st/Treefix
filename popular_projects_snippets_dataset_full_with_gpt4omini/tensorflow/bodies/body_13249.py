# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
x_shape = [7, 5, 4, 6]
param_shape = [6]
np.random.seed(1)  # Make it reproducible.
x_val = np.random.random_sample(x_shape).astype(np.float32)
m_val = np.random.random_sample(param_shape).astype(np.float32)
v_val = np.random.random_sample(param_shape).astype(np.float32)
beta_val = np.random.random_sample(param_shape).astype(np.float32)
gamma_val = np.random.random_sample(param_shape).astype(np.float32)
backprop_val = np.random.random_sample(x_shape).astype(np.float32)
for use_gpu in [False, True]:
    with self.cached_session(use_gpu=use_gpu) as sess:
        x = constant_op.constant(x_val, name="x")
        m = constant_op.constant(m_val, name="m")
        v = constant_op.constant(v_val, name="v")
        beta = constant_op.constant(beta_val, name="beta")
        gamma = constant_op.constant(gamma_val, name="gamma")
        backprop = constant_op.constant(backprop_val, name="backprop")
        epsilon = 0.001
        for scale_after_normalization in [True, False]:
            # _batch_norm_with_global_normalization_grad is deprecated in v9
            test_util.set_producer_version(ops.get_default_graph(), 8)
            grad = gen_nn_ops.batch_norm_with_global_normalization_grad(
                x, m, v, gamma, backprop, epsilon, scale_after_normalization)
            dx, dm, dv, db, dg = grad
            self.assertEqual(grad.dx, dx)
            self.assertEqual(grad.dm, dm)
            self.assertEqual(grad.dv, dv)
            self.assertEqual(grad.db, db)
            self.assertEqual(grad.dg, dg)

            on = self._opsBatchNorm(x, m, v, beta, gamma, epsilon,
                                    scale_after_normalization, True)
            odx, odm, odv, odb, odg = gradients_impl.gradients(
                [on], [x, m, v, beta, gamma], [backprop])
            if scale_after_normalization:
                all_grads = self.evaluate(
                    [dx, dm, dv, db, dg, odx, odm, odv, odb, odg])
                to_check = ["dx", "dm", "dv", "db", "dg"]
            else:
                all_grads = self.evaluate([dx, dm, dv, db, odx, odm, odv, odb])
                to_check = ["dx", "dm", "dv", "db"]
            for i, _ in enumerate(to_check):
                self.assertAllClose(
                    all_grads[i + len(to_check)], all_grads[i], atol=0.000001)
