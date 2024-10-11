# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv2d_backprop_filter_grad_test.py
if test.is_gpu_available(cuda_only=True):
    with self.session():
        for padding in [
            "SAME",
            "VALID",
            [(0, 0), (3, 5), (2, 1), (0, 0)],
            [(0, 0), (5, 2), (5, 1), (0, 0)]
        ]:
            for stride in [1, 2]:
                np.random.seed(1)
                in_shape = [5, 8, 6, 4]
                in_val = constant_op.constant(
                    2 * np.random.random_sample(in_shape) - 1, dtype=dtypes.float32)
                filter_shape = [3, 3, 4, 6]
                # Make a convolution op with the current settings,
                # just to easily get the shape of the output.
                conv_out = nn_ops.conv2d(
                    in_val,
                    array_ops.zeros(filter_shape),
                    dilations=[1, 2, 2, 1],
                    strides=[1, stride, stride, 1],
                    padding=padding)
                out_backprop_shape = conv_out.get_shape().as_list()
                out_backprop_val = constant_op.constant(
                    2 * np.random.random_sample(out_backprop_shape) - 1,
                    dtype=dtypes.float32)
                output = nn_ops.conv2d_backprop_filter(
                    in_val,
                    filter_shape,
                    out_backprop_val,
                    dilations=[1, 2, 2, 1],
                    strides=[1, stride, stride, 1],
                    padding=padding)
                err = gradient_checker.compute_gradient_error(
                    [in_val, out_backprop_val], [in_shape, out_backprop_shape],
                    output, filter_shape)
                print("conv2d_backprop_filter gradient err = %g " % err)
                err_tolerance = 1e-2
                self.assertLess(err, err_tolerance)
