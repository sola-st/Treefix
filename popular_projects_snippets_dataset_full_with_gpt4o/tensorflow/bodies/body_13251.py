# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
numpy_dtype = dtype.as_numpy_dtype
numpy_param_dtype = param_dtype.as_numpy_dtype
x_val = np.random.random_sample(x_shape).astype(numpy_dtype)
m_val = np.random.random_sample(param_shape).astype(numpy_param_dtype)
v_val = np.random.random_sample(param_shape).astype(numpy_param_dtype)
beta_val = np.random.random_sample(param_shape).astype(numpy_param_dtype)
gamma_val = np.random.random_sample(param_shape).astype(numpy_param_dtype)
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu) as sess:
        x = constant_op.constant(x_val, name="x")
        m = constant_op.constant(m_val, name="m")
        v = constant_op.constant(v_val, name="v")
        beta = constant_op.constant(beta_val, name="beta")
        gamma = constant_op.constant(gamma_val, name="gamma")
        epsilon = 0.001
        for scale_after_normalization in [True, False]:
            for shift_after_normalization in [True, False]:
                bn = self._tfBatchNormV2(x, m, v, beta, gamma, epsilon,
                                         scale_after_normalization,
                                         shift_after_normalization)
                np_batch_norm = self._npBatchNorm(x_val, m_val, v_val, beta_val,
                                                  gamma_val, epsilon,
                                                  scale_after_normalization,
                                                  shift_after_normalization)
                [tf_batch_norm] = self.evaluate([bn])
                self.assertEqual(x_shape, np_batch_norm.shape)
                self.assertEqual(x_shape, tf_batch_norm.shape)
                self.assertAllClose(np_batch_norm, tf_batch_norm, atol=atol)
