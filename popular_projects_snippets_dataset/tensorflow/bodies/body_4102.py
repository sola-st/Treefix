# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
np.random.seed(123)
row_window_size = 3
col_window_size = 4
window_size = [1, row_window_size, col_window_size, 1]
stride_size = [1, row_window_size - 1, col_window_size - 1, 1]

num_rows = (row_window_size - 1) * 5 + 1
num_cols = (col_window_size - 1) * 7 + 1
x_in = np.random.normal(0.0, 1.0, 2 * num_rows * num_cols * 3).reshape(
    [2, num_rows, num_cols, 3])
inputs = constant_op.constant(x_in, dtype=dtypes.float32)
with backprop.GradientTape() as tape:
    tape.watch([inputs])
    expected_result = nn_ops.max_pool_v2(inputs, window_size, stride_size,
                                         padding)
expected_grad = tape.gradient(expected_result, [inputs])

x = numpy_util.pack_numpy(
    inputs, Layout([self._dims[0]] + [layout_lib.UNSHARDED] * 3, self.mesh))

with api.run_on(self.mesh):
    with backprop.GradientTape() as tape:
        tape.watch([x])
        dtensor_result = nn_ops.max_pool_v2(x, window_size, stride_size,
                                            padding)
    dtensor_grad = tape.gradient(dtensor_result, [x])

self.assertDTensorEqual(
    expected_grad[0],
    Layout([self._dims[0]] + [layout_lib.UNSHARDED] * 3, self.mesh),
    dtensor_grad[0])
