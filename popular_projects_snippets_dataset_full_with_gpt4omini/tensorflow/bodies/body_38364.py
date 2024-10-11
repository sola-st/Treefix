# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for rank in range(1, _MAX_RANK + 1):
    np_arr = self._makeIncremental((2,) * rank, dtypes.float32)
    self._compareAllAxes(np_arr)

for _ in range(10):
    size_x = int(2**np.random.uniform(0, 15))
    size_y = int(2**np.random.uniform(0, 15))

    if size_x * size_y > 1e7:
        size_y = int(1e7 / size_x)

    arr = np.ones([size_x, size_y], dtype=np.float32)
    col_sum = np.sum(arr, axis=0)
    row_sum = np.sum(arr, axis=1)

    with self.session(graph=ops.Graph(), use_gpu=True) as sess:
        tf_row_sum = self._tf_reduce(arr, 1, False)
        tf_col_sum = self._tf_reduce(arr, 0, False)
        tf_out_row, tf_out_col = self.evaluate([tf_row_sum, tf_col_sum])
    self.assertAllClose(col_sum, tf_out_col)
    self.assertAllClose(row_sum, tf_out_row)

for size_x in [1, 3, 16, 33]:
    for size_y in [1, 3, 16, 33]:
        for size_z in [1, 3, 16, 33]:
            arr = np.ones([size_x, size_y, size_z], dtype=np.float32)
            sum_y = np.sum(arr, axis=1)
            sum_xz = np.sum(arr, axis=(0, 2))

            with self.session(graph=ops.Graph(), use_gpu=True) as sess:
                tf_sum_xz = self._tf_reduce(arr, [0, 2], False)
                tf_sum_y = self._tf_reduce(arr, 1, False)
                tf_out_sum_xz, tf_out_sum_y = self.evaluate([tf_sum_xz, tf_sum_y])
            self.assertAllClose(sum_y, tf_out_sum_y)
            self.assertAllClose(sum_xz, tf_out_sum_xz)
