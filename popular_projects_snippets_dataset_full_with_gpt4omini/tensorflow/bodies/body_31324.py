# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_conv2d_test.py
with self.session():
    # Input: [batch, height, width, input_depth]
    x_shape = [2, 5, 6, 2]
    # Filter: [kernel_height, kernel_width, input_depth, output_depth]
    f_shape = [3, 3, 2, 2]
    # Output: [batch, height, width, output_depth]
    y_shape = [2, 5, 6, 2]

    np.random.seed(1)  # Make it reproducible.
    x_val = np.random.random_sample(x_shape).astype(np.float32)
    f_val = np.random.random_sample(f_shape).astype(np.float32)
    x = constant_op.constant(x_val, name="x", dtype=dtypes.float32)
    f = constant_op.constant(f_val, name="f", dtype=dtypes.float32)

    for rate in range(1, 4):
        output = nn_ops.atrous_conv2d(x, f, rate=rate, padding="SAME")
        err = gradient_checker.compute_gradient_error([x, f],
                                                      [x_shape, f_shape],
                                                      output, y_shape)
        print("atrous_conv2d gradient err = %g " % err)
        err_tolerance = 4e-3 if test_util.is_xla_enabled() else 1e-3
        self.assertLess(err, err_tolerance)
