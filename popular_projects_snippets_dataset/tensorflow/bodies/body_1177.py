# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv3d_test.py
with self.session(), self.test_scope():
    strides = [1, 1, 1, 1, 1]

    # Input, output: [batch, depth, height, width, channel]
    x_shape = [2, 5, 6, 4, 3]
    y_shape = [2, 5, 6, 4, 2]

    # Filter: [kernel_depth, kernel_height, kernel_width, out_depth, in_depth]
    f_shape = [3, 3, 3, 2, 3]

    x = constant_op.constant(
        1.0, shape=x_shape, name="x", dtype=dtypes.float32)
    f = constant_op.constant(
        1.0, shape=f_shape, name="filter", dtype=dtypes.float32)
    output = nn_ops.conv3d_transpose(
        x, f, y_shape, strides=strides, padding="SAME")
    value = self.evaluate(output)

    # We count the number of cells being added at the locations in the output.
    # At the center, #cells = kernel_depth * kernel_height * kernel_width
    # At the corners, #cells = ceil(kernel_depth/2) * ceil(kernel_height/2)
    #                          * ceil(kernel_width/2)
    # At the edges, #cells =
    #   kernel_depth * ceil(kernel_height/2) * ceil(kernel_width/2) or
    #   ceil(kernel_depth/2) * kernel_height * ceil(kernel_width/2) or
    #   ceil(kernel_depth/2) * ceil(kernel_height/2) * kernel_width
    # At the borders, #cells =
    #   ceil(kernel_depth/2) * kernel_height * kernel_width or
    #   kernel_depth * ceil(kernel_height/2) * kernel_width or
    #   kernel_depth * kernel_height * ceil(kernel_width/2)

    for n in range(x_shape[0]):
        for k in range(f_shape[3]):
            for w in range(y_shape[3]):
                for h in range(y_shape[2]):
                    for d in range(y_shape[1]):
                        d_in = d > 0 and d < y_shape[1] - 1
                        h_in = h > 0 and h < y_shape[2] - 1
                        w_in = w > 0 and w < y_shape[3] - 1
                        if d_in + h_in + w_in == 3:
                            target = 27 * 3.0
                        elif d_in + h_in + w_in == 2:
                            target = 18 * 3.0
                        elif d_in or h_in or w_in:
                            target = 12 * 3.0
                        else:
                            target = 8 * 3.0
                        self.assertAllClose(target, value[n, d, h, w, k])
