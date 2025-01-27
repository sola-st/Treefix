# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_conv2d_test.py
"""Tests optimization of sequence of atrous convolutions.

    Verifies that a sequence of `atrous_conv2d` operations with identical `rate`
    parameters, 'SAME' `padding`, and `filters` with odd heights/ widths:

        net = atrous_conv2d(net, filters1, rate, padding="SAME")
        net = atrous_conv2d(net, filters2, rate, padding="SAME")
        ...
        net = atrous_conv2d(net, filtersK, rate, padding="SAME")

    is equivalent to:

        pad = ...  # padding so that the input dims are multiples of rate
        net = space_to_batch(net, paddings=pad, block_size=rate)
        net = conv2d(net, filters1, strides=[1, 1, 1, 1], padding="SAME")
        net = conv2d(net, filters2, strides=[1, 1, 1, 1], padding="SAME")
        ...
        net = conv2d(net, filtersK, strides=[1, 1, 1, 1], padding="SAME")
        net = batch_to_space(net, crops=pad, block_size=rate)
    """
padding = "SAME"  # The padding needs to be "SAME"
np.random.seed(1)  # Make it reproducible.

with self.session():
    # Input: [batch, height, width, input_depth]
    for height in range(15, 17):
        for width in range(15, 17):
            x_shape = [3, height, width, 2]
            x = np.random.random_sample(x_shape).astype(np.float32)

            for kernel in [1, 3, 5]:  # The kernel size needs to be odd.
                # Filter: [kernel_height, kernel_width, input_depth, output_depth]
                f_shape = [kernel, kernel, 2, 2]
                f = 1e-2 * np.random.random_sample(f_shape).astype(np.float32)

                for rate in range(2, 4):
                    # y1: three atrous_conv2d in a row.
                    y1 = nn_ops.atrous_conv2d(x, f, rate, padding=padding)
                    y1 = nn_ops.atrous_conv2d(y1, f, rate, padding=padding)
                    y1 = nn_ops.atrous_conv2d(y1, f, rate, padding=padding)
                    # y2: space_to_batch, three conv2d in a row, batch_to_space
                    pad_bottom = 0 if height % rate == 0 else rate - height % rate
                    pad_right = 0 if width % rate == 0 else rate - width % rate
                    pad = [[0, pad_bottom], [0, pad_right]]
                    y2 = array_ops.space_to_batch(x, paddings=pad, block_size=rate)
                    y2 = nn_ops.conv2d(y2, f, strides=[1, 1, 1, 1], padding=padding)
                    y2 = nn_ops.conv2d(y2, f, strides=[1, 1, 1, 1], padding=padding)
                    y2 = nn_ops.conv2d(y2, f, strides=[1, 1, 1, 1], padding=padding)
                    y2 = array_ops.batch_to_space(y2, crops=pad, block_size=rate)
                    self.assertAllClose(y1, y2, rtol=1e-2, atol=1e-2)
