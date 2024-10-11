# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv2d_transpose_test.py
with self.cached_session():
    for dtype in (dtypes.float32, dtypes.int32):
        strides = [1, 2, 2, 1]

        # Input, output: [batch, height, width, depth]
        x_shape = [2, 6, 4, 3]
        y_shape = [2, 13, 9, 2]

        # Filter: [kernel_height, kernel_width, output_depth, input_depth]
        f_shape = [3, 3, 2, 3]

        x = constant_op.constant(1, shape=x_shape, name="x", dtype=dtype)
        f = constant_op.constant(1, shape=f_shape, name="filter", dtype=dtype)
        output = nn_ops.conv2d_transpose(
            x, f, y_shape, strides=strides, padding="VALID")
        value = self.evaluate(output)

        cache_values = np.zeros(y_shape, dtype=np.float32)

        # The amount of padding added
        pad = 1

        for n in range(x_shape[0]):
            for k in range(f_shape[2]):
                for w in range(pad, y_shape[2] - pad):
                    for h in range(pad, y_shape[1] - pad):
                        target = 3
                        # We add a case for locations divisible by the stride.
                        h_in = h % strides[1] == 0 and h > pad and h < y_shape[
                            1] - 1 - pad
                        w_in = w % strides[2] == 0 and w > pad and w < y_shape[
                            2] - 1 - pad
                        if h_in and w_in:
                            target += 9
                        elif h_in or w_in:
                            target += 3
                        cache_values[n, h, w, k] = target

            # copy values in the border
                cache_values[n, :, 0, k] = cache_values[n, :, 1, k]
                cache_values[n, :, -1, k] = cache_values[n, :, -2, k]
                cache_values[n, 0, :, k] = cache_values[n, 1, :, k]
                cache_values[n, -1, :, k] = cache_values[n, -2, :, k]

        if dtype.is_integer:
            self.assertAllEqual(cache_values, value)
        else:
            self.assertAllClose(cache_values, value)
