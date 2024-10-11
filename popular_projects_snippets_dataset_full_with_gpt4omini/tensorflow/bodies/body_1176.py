# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv3d_test.py
with self.session(), self.test_scope():
    for padding in ["SAME", "VALID"]:
        for stride in [1, 2]:
            np.random.seed(1)
            in_shape = [2, 4, 3, 3, 2]
            in_val = constant_op.constant(
                2 * np.random.random_sample(in_shape) - 1, dtype=dtypes.float32)
            filter_shape = [3, 3, 3, 2, 3]
            strides = [1, stride, stride, stride, 1]
            # Make a convolution op with the current settings, just to easily get
            # the shape of the output.
            conv_out = nn_ops.conv3d(in_val,
                                     array_ops.zeros(filter_shape), strides,
                                     padding)
            out_backprop_shape = conv_out.get_shape().as_list()
            out_backprop_val = constant_op.constant(
                2 * np.random.random_sample(out_backprop_shape) - 1,
                dtype=dtypes.float32)
            output = nn_ops.conv3d_backprop_filter_v2(in_val, filter_shape,
                                                      out_backprop_val, strides,
                                                      padding)
            err = gradient_checker.compute_gradient_error(
                [in_val, out_backprop_val], [in_shape, out_backprop_shape],
                output, filter_shape)
            print("conv3d_backprop_filter gradient err = %g " % err)
            err_tolerance = 1e-3
            self.assertLess(err, err_tolerance)
