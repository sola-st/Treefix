# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv2d_transpose_test.py
with self.cached_session():
    for dtype in (dtypes.float32, dtypes.int32):
        strides = [1, 2, 2, 1]

        # Input, output: [batch, height, width, depth]
        x_shape = [2, 6, 4, 3]
        y_shape = [2, 12, 8, 2]

        # Filter: [kernel_height, kernel_width, output_depth, input_depth]
        f_shape = [3, 3, 2, 3]

        x = constant_op.constant(1, shape=x_shape, name="x", dtype=dtype)
        f = constant_op.constant(1, shape=f_shape, name="filter", dtype=dtype)
        output = nn_ops.conv2d_transpose(
            x, f, y_shape, strides=strides, padding="SAME")
        value = self.evaluate(output)

        for n in range(x_shape[0]):
            for k in range(f_shape[2]):
                for w in range(y_shape[2]):
                    for h in range(y_shape[1]):
                        target = 3
                        # We add a case for locations divisible by the stride.
                        h_in = h % strides[1] == 0 and h > 0 and h < y_shape[1] - 1
                        w_in = w % strides[2] == 0 and w > 0 and w < y_shape[2] - 1
                        if h_in and w_in:
                            target += 9
                        elif h_in or w_in:
                            target += 3

                        if dtype.is_integer:
                            self.assertAllEqual(target, value[n, h, w, k])
                        else:
                            self.assertAllClose(target, value[n, h, w, k])
