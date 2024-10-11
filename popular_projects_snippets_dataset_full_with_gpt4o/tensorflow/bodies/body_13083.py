# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
for mu in [0.0, 1.0, 1e3]:
    for sigma in [1.0, 0.1]:
        for keep_dims in [True, False]:
            input_values = np.random.rand(*input_shape) * sigma + mu
            expected_mean = np.mean(
                input_values, axis=moments_axes, keepdims=keep_dims)
            expected_var = np.var(
                input_values, axis=moments_axes, keepdims=keep_dims)
            with ops.Graph().as_default() as g:
                with self.session(graph=g) as sess:
                    inputs = constant_op.constant(
                        input_values, shape=input_shape, dtype=dtypes.float32)
                    mean, variance = nn_impl.moments_v2(
                        inputs, moments_axes, keepdims=keep_dims)

                    if check_gradients:
                        err = gradient_checker.compute_gradient_error(
                            inputs, input_shape, mean, mean.shape.as_list())
                        self.assertLess(err, 1e-3)
                        err = gradient_checker.compute_gradient_error(
                            inputs, input_shape, variance, variance.shape.as_list())
                        self.assertLess(err, 1e-3)

                    # Evaluate.
                    [mean, variance] = self.evaluate([mean, variance])
                    # Make sure that there are no NaNs
                    self.assertFalse(np.isnan(mean).any())
                    self.assertFalse(np.isnan(variance).any())
                    self.assertAllClose(mean, expected_mean, rtol=tol, atol=tol)
                    self.assertAllClose(variance, expected_var, rtol=tol, atol=tol)
