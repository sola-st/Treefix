# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
with self.cached_session():
    # shape = [batch, width, height, depth]
    assert len(shape) == 4

    x_numpy = np.random.normal(size=shape).astype(np.float32)
    x = math_ops.cast(constant_op.constant(x_numpy), dtype=dtype)

    # Compute the expected values at high precision since the method
    # is prone to catastrophic cancellation:
    x_numpy = x_numpy.astype(np.float128)

    mean, var = self._unweighted_moments(x, axes, keep_dims=keep_dims)

    num_elements = np.prod([shape[i] for i in axes])

    ax = tuple(axes)
    expected_mean = np.sum(x_numpy, axis=ax,
                           keepdims=keep_dims) / num_elements
    expected_mean_squared = np.multiply(expected_mean, expected_mean)
    expected_x_squared = np.sum(np.multiply(x_numpy, x_numpy),
                                axis=ax,
                                keepdims=keep_dims) / num_elements
    expected_variance = expected_x_squared - expected_mean_squared

    # Check that the moments are correct.
    self.assertAllCloseAccordingToType(expected_mean, self.evaluate(mean))
    self.assertAllCloseAccordingToType(expected_variance, self.evaluate(var))
