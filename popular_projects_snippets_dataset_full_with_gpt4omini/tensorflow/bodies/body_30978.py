# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv1d_transpose_test.py
with self.cached_session():
    strides = [1, 1, 1]

    # Input, output: [batch, width, depth]
    x_shape = [2, 6, 3]
    y_shape = [2, 6, 2]

    # Filter: [kernel_width, output_depth, input_depth]
    f_shape = [3, 2, 3]

    x = constant_op.constant(
        1.0, shape=x_shape, name="x", dtype=dtypes.float32)
    f = constant_op.constant(
        1.0, shape=f_shape, name="filter", dtype=dtypes.float32)
    output = nn_ops.conv1d_transpose(
        x, f, y_shape, strides=strides, padding="SAME")
    value = self.evaluate(output)

    for n in range(y_shape[0]):
        for w in range(y_shape[1]):
            for c in range(y_shape[2]):
                target = 2 * 3.0
                w_in = w > 0 and w < y_shape[1] - 1
                if w_in:
                    target += 3.0
                self.assertAllClose(target, value[n, w, c])
