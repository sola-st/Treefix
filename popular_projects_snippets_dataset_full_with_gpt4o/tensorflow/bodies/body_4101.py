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
expected_result = nn_ops.max_pool_v2(inputs, window_size, stride_size,
                                     padding)

x = numpy_util.pack_numpy(
    inputs, Layout([self._dims[0]] + [layout_lib.UNSHARDED] * 3, self.mesh))

got = nn_ops.max_pool_v2(x, window_size, stride_size, padding)

self.assertDTensorEqual(
    expected_result,
    Layout([self._dims[0]] + [layout_lib.UNSHARDED] * 3, self.mesh), got)
