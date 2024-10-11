# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bitwise_ops_test.py
dtype_list = [dtypes.int8, dtypes.int16, dtypes.int32, dtypes.int64,
              dtypes.uint8, dtypes.uint16, dtypes.uint32, dtypes.uint64]

with self.session() as sess:
    for dtype in dtype_list:
        lhs = constant_op.constant([0, 5, 3, 14], dtype=dtype)
        rhs = constant_op.constant([5, 0, 7, 11], dtype=dtype)
        and_result, or_result, xor_result = sess.run(
            [bitwise_ops.bitwise_and(lhs, rhs),
             bitwise_ops.bitwise_or(lhs, rhs),
             bitwise_ops.bitwise_xor(lhs, rhs)])
        self.assertAllEqual(and_result, [0, 0, 3, 10])
        self.assertAllEqual(or_result, [5, 5, 7, 15])
        self.assertAllEqual(xor_result, [5, 5, 4, 5])
