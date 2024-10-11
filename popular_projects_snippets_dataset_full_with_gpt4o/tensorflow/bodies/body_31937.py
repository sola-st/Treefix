# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv1d_test.py
with self.cached_session():
    stride = 2

    # Input, output: [batch, width, depth]
    x_shape = [2, 4, 3]
    y_shape = [2, 9, 2]

    # Filter: [kernel_width, output_depth, input_depth]
    f_shape = [3, 2, 3]

    x = constant_op.constant(
        1.0, shape=x_shape, name="x", dtype=dtypes.float32)
    f = constant_op.constant(
        1.0, shape=f_shape, name="filter", dtype=dtypes.float32)
    output = nn_ops.conv1d_transpose(
        x, f, y_shape, strides=stride, padding="VALID")
    value = self.evaluate(output)

    cache_values = np.zeros(y_shape, dtype=np.float32)

    # The amount of padding added
    pad = 1

    for n in range(x_shape[0]):
        for k in range(f_shape[1]):
            for w in range(pad, y_shape[1] - pad):
                target = 3.0
                # We add a case for locations divisible by the stride.
                w_in = w % stride == 0 and w > pad and w < y_shape[1] - 1 - pad
                if w_in:
                    target += 3.0
                cache_values[n, w, k] = target

            # copy values in the border
            cache_values[n, 0, k] = cache_values[n, 1, k]
            cache_values[n, -1, k] = cache_values[n, -2, k]

self.assertAllClose(cache_values, value)
