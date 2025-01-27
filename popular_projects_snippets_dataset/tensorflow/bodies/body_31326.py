# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_conv2d_test.py
with self.session():
    # Input: [batch, height, width, input_depth]
    height = 9
    for width in [9, 10]:  # Test both odd and even width.
        x_shape = [2, height, width, 2]
        x = np.arange(np.prod(x_shape), dtype=np.float32).reshape(x_shape)

        # Filter: [kernel_height, kernel_width, input_depth, output_depth]
        for kernel_height in range(1, 4):
            for kernel_width in range(1, 4):
                f_shape = [kernel_height, kernel_width, 2, 2]
                f = np.arange(np.prod(f_shape), dtype=np.float32).reshape(f_shape)

                for rate in range(1, 4):
                    f_up = _upsample_filters(f, rate)
                    kernel_height_up = (kernel_height + (kernel_height - 1) *
                                        (rate - 1))
                    kernel_width_up = kernel_width + (kernel_width - 1) * (rate - 1)

                    for padding in ["SAME", "VALID"]:
                        if padding == "SAME":
                            y_shape = [2, height, width, 2]
                        else:
                            y_shape = [
                                2, height + kernel_height_up - 1,
                                width + kernel_width_up - 1, 2
                            ]

                        y1 = nn_ops.atrous_conv2d_transpose(x, f, y_shape, rate,
                                                            padding)
                        y2 = nn_ops.conv2d_transpose(
                            x, f_up, y_shape, strides=[1, 1, 1, 1], padding=padding)
                        self.assertAllClose(y1, y2, rtol=1e-3, atol=1e-3)
