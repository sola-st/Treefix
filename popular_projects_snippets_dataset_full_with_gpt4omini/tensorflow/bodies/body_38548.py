# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test_big.py
# make sure we test all possible kernel invocations
# logic is the same for all ops, test just float32 for brevity
arr_ = np.ones([4097, 4097], dtype=np.float32)
for size_x in [
    1, 2, 3, 4, 16, 17, 32, 33, 64, 65, 128, 131, 256, 263, 1024, 1025,
    4096, 4097
]:
    for size_y in [
        1, 2, 3, 4, 16, 17, 32, 33, 64, 65, 128, 131, 256, 263, 1024, 1025,
        4096, 4097
    ]:
        arr = arr_[0:size_x, 0:size_y]
        col_sum = np.ones([size_y], dtype=np.float32) * size_x
        row_sum = np.ones([size_x], dtype=np.float32) * size_y
        full_sum = np.ones([], dtype=np.float32) * size_x * size_y

        with self.session(graph=ops.Graph(), use_gpu=True) as sess:
            arr_placeholder = array_ops.placeholder(dtype=np.float32,
                                                    shape=(size_x, size_y))
            tf_row_sum = self._tf_reduce_sum(arr_placeholder, 1, False)
            tf_col_sum = self._tf_reduce_sum(arr_placeholder, 0, False)
            tf_full_sum = self._tf_reduce_sum(arr_placeholder, [0, 1], False)
            tf_out_row, tf_out_col, tf_out_full = sess.run(
                [tf_row_sum, tf_col_sum, tf_full_sum], {arr_placeholder: arr})
        self.assertAllClose(col_sum, tf_out_col)
        self.assertAllClose(row_sum, tf_out_row)
        self.assertAllClose(full_sum, tf_out_full)

arr_ = np.ones([130, 130, 130], dtype=np.float32)
for size_x in range(1, 130, 13):
    for size_y in range(1, 130, 13):
        for size_z in range(1, 130, 13):
            arr = arr_[0:size_x, 0:size_y, 0:size_z]
            sum_y = np.ones([size_x, size_z], dtype=np.float32)
            sum_xz = np.ones([size_y], dtype=np.float32)

            with self.session(graph=ops.Graph(), use_gpu=True) as sess:
                arr_placeholder = array_ops.placeholder(
                    dtype=np.float32, shape=(size_x, size_y, size_z))
                tf_sum_xz = self._tf_reduce_mean(arr_placeholder, [0, 2], False)
                tf_sum_y = self._tf_reduce_mean(arr_placeholder, 1, False)
                tf_out_sum_xz, tf_out_sum_y = sess.run([tf_sum_xz, tf_sum_y],
                                                       {arr_placeholder: arr})
            self.assertAllClose(sum_y, tf_out_sum_y)
            self.assertAllClose(sum_xz, tf_out_sum_xz)
