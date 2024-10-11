# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv3d_test.py
with self.session(), self.test_scope():
    strides = [1, 2, 2, 2, 1]

    # Input, output: [batch, depth, height, width, depth]
    x_shape = [2, 5, 6, 4, 3]
    y_shape = [2, 11, 13, 9, 2]

    # Filter: [kernel_depth, kernel_height, kernel_width, out_depth, in_depth]
    f_shape = [3, 3, 3, 2, 3]

    x = constant_op.constant(
        1.0, shape=x_shape, name="x", dtype=dtypes.float32)
    f = constant_op.constant(
        1.0, shape=f_shape, name="filter", dtype=dtypes.float32)
    output = nn_ops.conv3d_transpose(
        x, f, y_shape, strides=strides, padding="VALID")
    value = self.evaluate(output)

    cache_values = np.zeros(y_shape, dtype=np.float32)

    # The amount of padding added
    pad = 1

    for n in range(x_shape[0]):
        for k in range(f_shape[3]):
            for w in range(y_shape[3]):
                for h in range(y_shape[2]):
                    for d in range(y_shape[1]):
                        # We add a case for locations divisible by the stride.
                        d_in = d % strides[1] == 0 and pad < d < y_shape[1] - 1 - pad
                        h_in = h % strides[2] == 0 and pad < h < y_shape[2] - 1 - pad
                        w_in = w % strides[3] == 0 and pad < w < y_shape[3] - 1 - pad
                        if d_in + h_in + w_in == 3:
                            target = 8 * 3.0
                        elif d_in + h_in + w_in == 2:
                            target = 4 * 3.0
                        elif d_in or h_in or w_in:
                            target = 2 * 3.0
                        else:
                            target = 3.0
                        cache_values[n, d, h, w, k] = target

          # copy values in the border
            cache_values[n, :, :, 0, k] = cache_values[n, :, :, 1, k]
            cache_values[n, :, :, -1, k] = cache_values[n, :, :, -2, k]
            cache_values[n, :, 0, :, k] = cache_values[n, :, 1, :, k]
            cache_values[n, :, -1, :, k] = cache_values[n, :, -2, :, k]
            cache_values[n, 0, :, :, k] = cache_values[n, 1, :, :, k]
            cache_values[n, -1, :, :, k] = cache_values[n, -2, :, :, k]

self.assertAllClose(cache_values, value)
