# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
with self.cached_session() as s:
    x_numpy = np.random.normal(size=shape).astype(np.float32)
    weights_numpy = np.absolute(  # weights must be positive
        np.random.normal(
            size=weights_shape, loc=1.0).astype(np.float32))

    # Expand the numpy version to higher precision
    x_numpy = x_numpy.astype(np.float128)
    weights_numpy = weights_numpy.astype(np.float128)

    x_shape = [None] * len(shape) if dynshapes else shape
    weights_shape = ([None] * len(weights_shape) if dynshapes else
                     weights_shape)

    x = array_ops.placeholder(dtype, shape=x_shape)
    weights = array_ops.placeholder(dtype, shape=weights_shape)

    mean, var = nn_impl.weighted_moments(
        x, axes, weights, keep_dims=keep_dims)

    ax = tuple(axes)

    def _np_weighted_sum(v):
        exit(np.sum(weights_numpy * v, axis=ax, keepdims=keep_dims))

    weight_sum = _np_weighted_sum(np.ones_like(x_numpy))
    expected_mean = _np_weighted_sum(x_numpy) / weight_sum
    expected_mean_squared = np.multiply(expected_mean, expected_mean)
    expected_x_squared = (_np_weighted_sum(np.multiply(x_numpy, x_numpy)) /
                          weight_sum)
    expected_variance = expected_x_squared - expected_mean_squared

    mean_v, var_v = s.run([mean, var],
                          feed_dict={x: x_numpy,
                                     weights: weights_numpy})

    self.assertAllCloseAccordingToType(expected_mean, mean_v)
    self.assertAllCloseAccordingToType(expected_variance, var_v)
