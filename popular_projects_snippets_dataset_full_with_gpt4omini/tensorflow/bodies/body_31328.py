# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_conv2d_test.py
strides = [1, 1, 1, 1]
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

                    for padding in ["SAME", "VALID"]:
                        y1 = nn_impl.depthwise_conv2d(
                            x, f, strides, padding, rate=[rate, rate])
                        y2 = nn_impl.depthwise_conv2d(x, f_up, strides, padding)
                        self.assertAllClose(y1, y2, rtol=1e-3, atol=1e-3)
