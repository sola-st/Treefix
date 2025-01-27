# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
x_shape = [3, 5, 4, 5]
param_shape = [5]
np.random.seed(1)  # Make it reproducible.
x_val = np.random.random_sample(x_shape).astype(np.float64)
m_val = np.random.random_sample(param_shape).astype(np.float64)
v_val = np.random.random_sample(param_shape).astype(np.float64)
beta_val = np.random.random_sample(param_shape).astype(np.float64)
gamma_val = np.random.random_sample(param_shape).astype(np.float64)
with self.cached_session():
    x = constant_op.constant(x_val, name="x")
    m = constant_op.constant(m_val, name="m")
    v = constant_op.constant(v_val, name="v")
    beta = constant_op.constant(beta_val, name="beta")
    gamma = constant_op.constant(gamma_val, name="gamma")
    epsilon = 0.001
    if version == 1:
        output = self._tfBatchNormV1(x, m, v, beta, gamma, epsilon,
                                     scale_after_normalization)
    elif version == 2:
        output = self._tfBatchNormV2(x, m, v, beta, gamma, epsilon,
                                     scale_after_normalization,
                                     shift_after_normalization)
    else:
        print("Invalid version", version)
        raise ValueError()
    all_params = [x, m, v, beta, gamma]
    all_shapes = [x_shape, param_shape, param_shape, param_shape, param_shape]
    err = gradient_checker.compute_gradient_error(all_params[param_index],
                                                  all_shapes[param_index],
                                                  output, x_shape)
print("Batch normalization v%d %s gradient %s scale and %s shift err = " %
      (version, tag, "with" if scale_after_normalization else "without",
       "with" if shift_after_normalization else "without"), err)
self.assertLess(err, err_tolerance)
