# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bitwise_ops_test.py
dtype_list = [dtypes.int8, dtypes.int16, dtypes.int32, dtypes.int64,
              dtypes.uint8, dtypes.uint16]

with self.session() as sess:
    for dtype in dtype_list:
        lhs = constant_op.constant([[0], [3], [5]], dtype=dtype)
        rhs = constant_op.constant([[1, 2, 4]], dtype=dtype)

        and_tensor = bitwise_ops.bitwise_and(lhs, rhs)
        or_tensor = bitwise_ops.bitwise_or(lhs, rhs)
        xor_tensor = bitwise_ops.bitwise_xor(lhs, rhs)
        ls_tensor = bitwise_ops.left_shift(lhs, rhs)
        rs_tensor = bitwise_ops.right_shift(lhs, rhs)

        and_result, or_result, xor_result, ls_result, rs_result = sess.run(
            [and_tensor, or_tensor, xor_tensor, ls_tensor, rs_tensor])

        # Compare shape inference with result
        self.assertAllEqual(and_tensor.get_shape().as_list(), and_result.shape)
        self.assertAllEqual(and_tensor.get_shape().as_list(), [3, 3])
        self.assertAllEqual(or_tensor.get_shape().as_list(), or_result.shape)
        self.assertAllEqual(or_tensor.get_shape().as_list(), [3, 3])
        self.assertAllEqual(xor_tensor.get_shape().as_list(), xor_result.shape)
        self.assertAllEqual(xor_tensor.get_shape().as_list(), [3, 3])
        self.assertAllEqual(ls_tensor.get_shape().as_list(), ls_result.shape)
        self.assertAllEqual(ls_tensor.get_shape().as_list(), [3, 3])
        self.assertAllEqual(rs_tensor.get_shape().as_list(), rs_result.shape)
        self.assertAllEqual(rs_tensor.get_shape().as_list(), [3, 3])
