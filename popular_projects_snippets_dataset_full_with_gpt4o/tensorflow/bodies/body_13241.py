# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
x_shape = [3, 5, 4, 2]
param_shape = [2]
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
        epsilon = 0.001
        for scale_after_normalization in [True, False]:
            for shift_after_normalization in [True, False]:
                bn2 = self._tfBatchNormV2(x, m, v, beta, gamma, epsilon,
                                          scale_after_normalization,
                                          shift_after_normalization)
                bn1bw = self._tfBatchNormV1BW(x, m, v, beta, gamma, epsilon,
                                              scale_after_normalization)
                bn1 = self._tfBatchNormV1(x, m, v, beta, gamma, epsilon,
                                          scale_after_normalization)
                on = self._opsBatchNorm(x, m, v, beta, gamma, epsilon,
                                        scale_after_normalization,
                                        shift_after_normalization)
                np_bn = self._npBatchNorm(x_val, m_val, v_val, beta_val, gamma_val,
                                          epsilon, scale_after_normalization,
                                          shift_after_normalization)
                tf_bn_v2, tf_bn_v1bw, tf_bn_v1, ops_bn = sess.run(
                    [bn2, bn1bw, bn1, on])
                self.assertAllClose(np_bn, ops_bn, atol=0.00001)
                self.assertAllClose(np_bn, tf_bn_v2, atol=0.00001)
                self.assertAllClose(tf_bn_v2, ops_bn, atol=0.00001)
                # shift_after_normalization=False is not supported in v1.
                if shift_after_normalization:
                    self.assertAllClose(np_bn, tf_bn_v1bw, atol=0.00001)
                    self.assertAllClose(np_bn, tf_bn_v1, atol=0.00001)
                    self.assertAllClose(tf_bn_v1, ops_bn, atol=0.00001)
                    self.assertAllClose(tf_bn_v1bw, ops_bn, atol=0.00001)
