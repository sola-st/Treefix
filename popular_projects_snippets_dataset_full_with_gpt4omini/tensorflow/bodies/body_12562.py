# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bitwise_ops_test.py
dtype_list = [np.int8, np.int16, np.int32, np.int64,
              np.uint8, np.uint16, np.uint32, np.uint64]

with self.session() as sess:
    for dtype in dtype_list:
        lhs = np.array([0, 5, 3, 14], dtype=dtype)
        rhs = np.array([5, 0, 7, 3], dtype=dtype)
        left_shift_result, right_shift_result = sess.run(
            [bitwise_ops.left_shift(lhs, rhs),
             bitwise_ops.right_shift(lhs, rhs)])
        self.assertAllEqual(left_shift_result, np.left_shift(lhs, rhs))
        self.assertAllEqual(right_shift_result, np.right_shift(lhs, rhs))
