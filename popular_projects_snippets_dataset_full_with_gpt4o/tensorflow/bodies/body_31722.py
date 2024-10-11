# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv3d_transpose_test.py
with self.cached_session():
    x_value = np.zeros([10, 0, 2, 3, 3])
    f_value = np.ones((3, 3, 3, 3, 3))
    y_shape = np.stack([10, 0, 2, 3, 3])
    output = nn_ops.conv3d_transpose(
        x_value,
        f_value,
        y_shape,
        strides=(1, 1, 1),
        data_format="NDHWC",
        padding="SAME",
    )
    _ = self.evaluate(output)
