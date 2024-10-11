# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv1d_transpose_test.py
with self.cached_session():
    strides = [1, 2, 1]

    # Input, output: [batch, width, depth]
    x_shape = [2, 4, 3]
    y_shape = [2, 8, 2]

    # Filter: [kernel_width, output_depth, input_depth]
    f_shape = [3, 2, 3]

    x = constant_op.constant(
        1.0, shape=x_shape, name="x", dtype=dtypes.float32)
    f = constant_op.constant(
        1.0, shape=f_shape, name="filter", dtype=dtypes.float32)
    output = nn_ops.conv1d_transpose(
        x, f, y_shape, strides=strides, padding="SAME")
    value = self.evaluate(output)

    for n in range(x_shape[0]):
        for k in range(f_shape[1]):
            for w in range(y_shape[1]):
                target = 3.0
                # We add a case for locations divisible by the stride.
                w_in = w % strides[1] == 0 and w > 0 and w < y_shape[1] - 1
                if w_in:
                    target += 3.0
                self.assertAllClose(target, value[n, w, k])
