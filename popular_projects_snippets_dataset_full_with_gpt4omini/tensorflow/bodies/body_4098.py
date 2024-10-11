# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
np.random.seed(123)

x_in = np.random.normal(0.0, 1.0, 9 * 9).reshape([1, 9, 9, 1])
kernel_in = np.array([
    [[[2, 0.1]], [[3, 0.2]]],
    [[[0, 0.3]], [[1, 0.4]]],
])

x = constant_op.constant(x_in, dtype=dtypes.float32)
kernel = constant_op.constant(kernel_in, dtype=dtypes.float32)
expected_result = nn_ops.conv2d_v2(
    x, kernel, strides=[1, 1, 1, 1], padding=padding)

x = api.copy_to_mesh(x, Layout([layout_lib.UNSHARDED] * 4, self.mesh))
kernel = api.copy_to_mesh(kernel,
                          Layout([layout_lib.UNSHARDED] * 4, self.mesh))

got = nn_ops.conv2d_v2(x, kernel, strides=[1, 1, 1, 1], padding=padding)

self.assertDTensorEqual(expected_result,
                        Layout([layout_lib.UNSHARDED] * 4, self.mesh), got)
