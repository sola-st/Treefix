# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
with self.cached_session():
    x_shape = [3, 5, 4, 2]
    x_val = np.random.random_sample(x_shape).astype(np.float64)
    x = constant_op.constant(x_val)
    x.set_shape(x_shape)

    axes = [0, 1, 2]
    y_shape = [2]  # Depth of x

    inputs_to_compute_gradients_for = [x]

    out_mean, out_var = self._unweighted_moments(
        x, axes, extra_out_grads=inputs_to_compute_gradients_for)
    if from_y == "mean":
        y = out_mean
    elif from_y == "var":
        y = out_var

    for (i, v) in enumerate(inputs_to_compute_gradients_for):
        err = gradient_checker.compute_gradient_error(v,
                                                      v.get_shape().as_list(),
                                                      y, y_shape)
        print("Moments %s gradient err vs input %d = %g" % (from_y, i, err))
        self.assertLess(err, 1e-11)
