# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv3d_transpose_test.py
# Test case for GitHub issue 18887
for dtype in [dtypes.int32, dtypes.int64]:
    with self.cached_session():
        x_shape = [2, 5, 6, 4, 3]
        y_shape = [2, 5, 6, 4, 2]
        f_shape = [3, 3, 3, 2, 3]
        strides = [1, 1, 1, 1, 1]
        x_value = constant_op.constant(
            1.0, shape=x_shape, name="x", dtype=dtypes.float32)
        f_value = constant_op.constant(
            1.0, shape=f_shape, name="filter", dtype=dtypes.float32)
        output = nn_ops.conv3d_transpose(
            x_value, f_value, constant_op.constant(y_shape, dtype=dtype),
            strides=strides, padding="SAME")
        self.evaluate(output)
