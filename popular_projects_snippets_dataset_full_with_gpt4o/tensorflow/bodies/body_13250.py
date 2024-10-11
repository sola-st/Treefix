# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
"""Test for tf.nn.moments(..., keep_dims=True / False).

    Make sure that parameters with shape (1, 1, 1, depth) yield the same
    result as parameters with shape (depth)
    """
x_shape = (3, 5, 4, 2)
param_shape = (2)
keep_dims_param_shape = (1, 1, 1, 2)
x_val = np.random.random_sample(x_shape).astype(np.float32)
m_val = np.random.random_sample(param_shape).astype(np.float32)
v_val = np.random.random_sample(param_shape).astype(np.float32)
beta_val = np.random.random_sample(param_shape).astype(np.float32)
gamma_val = np.random.random_sample(param_shape).astype(np.float32)
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu) as sess:
        x = constant_op.constant(x_val, name="x")
        m = constant_op.constant(m_val, name="m")
        v = constant_op.constant(v_val, name="v")
        beta = constant_op.constant(beta_val, name="beta")
        gamma = constant_op.constant(gamma_val, name="gamma")
        keep_dims_m = array_ops.reshape(
            m, keep_dims_param_shape, name="keep_dims_m")
        keep_dims_v = array_ops.reshape(
            v, keep_dims_param_shape, name="keep_dims_v")
        keep_dims_beta = array_ops.reshape(
            beta, keep_dims_param_shape, name="keep_dims_beta")
        keep_dims_gamma = array_ops.reshape(
            gamma, keep_dims_param_shape, name="keep_dims_gamma")
        epsilon = 0.001
        for scale_after_normalization in [True, False]:
            for shift_after_normalization in [True, False]:
                bn = self._tfBatchNormV2(x, m, v, beta, gamma, epsilon,
                                         scale_after_normalization,
                                         shift_after_normalization)
                keep_dims_bn = self._tfBatchNormV2(x, keep_dims_m, keep_dims_v,
                                                   keep_dims_beta, keep_dims_gamma,
                                                   epsilon,
                                                   scale_after_normalization,
                                                   shift_after_normalization)
                tf_batch_norm, keep_dims_tf_batch_norm = sess.run(
                    [bn, keep_dims_bn])
                self.assertEqual(x_shape, tf_batch_norm.shape)
                self.assertEqual(x_shape, keep_dims_tf_batch_norm.shape)
                self.assertAllClose(
                    tf_batch_norm, keep_dims_tf_batch_norm, atol=0.000001)
