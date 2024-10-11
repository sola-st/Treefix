# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
# Reason to flip same shape policy: The backprop of the nn_ops.conv2d_v2 is
# simply array_ops.ones_like_v2(conv2d_result). However, as DTensor does not
# control gradient tape, the tape will not attach the layout from
# conv2d_result to the ones. In normal computation, the backprop pass has
# more information to pass from the final scalar loss to the conv2d, so
# this is not a problem.
# But this well-design unit tests, without same shape policy, it will get a
# different layout for the inputs' grad.
api._dtensor_device().set_same_shape_policy(True)

np.random.seed(123)

x_in = np.random.normal(0.0, 1.0, 2 * 9 * 9).reshape([2, 9, 9, 1])
kernel_in = np.array([
    [[[2, 0.1]], [[3, 0.2]]],
    [[[0, 0.3]], [[1, 0.4]]],
])

x = constant_op.constant(x_in, dtype=dtypes.float32)
kernel = constant_op.constant(kernel_in, dtype=dtypes.float32)
with backprop.GradientTape() as tape:
    tape.watch([x, kernel])
    expected_result = nn_ops.conv2d_v2(
        x, kernel, strides=[1, 1, 1, 1], padding=padding)
expected_input_gradient, expected_filter_gradient = tape.gradient(
    expected_result, [x, kernel])

x = numpy_util.pack_numpy(
    x, Layout([self._dims[0]] + [layout_lib.UNSHARDED] * 3, self.mesh))
kernel = api.copy_to_mesh(kernel,
                          Layout([layout_lib.UNSHARDED] * 4, self.mesh))

# Explicitly open the scope as ops generated from tape could be broadcasted
# to replicated by default.
with api.run_on(self.mesh):
    with backprop.GradientTape() as tape:
        tape.watch([x, kernel])
        got = nn_ops.conv2d_v2(x, kernel, strides=[1, 1, 1, 1], padding=padding)
    got_input_gradient, got_filter_filter = tape.gradient(got, [x, kernel])

self.assertDTensorEqual(
    expected_result,
    Layout([self._dims[0]] + [layout_lib.UNSHARDED] * 3, self.mesh), got)
self.assertDTensorEqual(
    expected_input_gradient,
    Layout([self._dims[0]] + [layout_lib.UNSHARDED] * 3, self.mesh),
    got_input_gradient)
self.assertDTensorEqual(expected_filter_gradient,
                        Layout([layout_lib.UNSHARDED] * 4, self.mesh),
                        got_filter_filter)
api._dtensor_device().set_same_shape_policy(False)
