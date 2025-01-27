# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bitwise_ops_test.py
dtype_list = [dtypes.int8, dtypes.int16, dtypes.int32, dtypes.int64,
              dtypes.uint8, dtypes.uint16, dtypes.uint32, dtypes.uint64]
inputs = [0, 5, 3, 14]
with self.session() as sess:
    for dtype in dtype_list:
        # Because of issues with negative numbers, let's test this indirectly.
        # 1. invert(a) and a = 0
        # 2. invert(a) or a = invert(0)
        input_tensor = constant_op.constant(inputs, dtype=dtype)
        not_a_and_a, not_a_or_a, not_0 = sess.run(
            [bitwise_ops.bitwise_and(
                input_tensor, bitwise_ops.invert(input_tensor)),
             bitwise_ops.bitwise_or(
                 input_tensor, bitwise_ops.invert(input_tensor)),
             bitwise_ops.invert(constant_op.constant(0, dtype=dtype))])
        self.assertAllEqual(not_a_and_a, [0, 0, 0, 0])
        self.assertAllEqual(not_a_or_a, [not_0] * 4)
        # For unsigned dtypes let's also check the result directly.
        if dtype.is_unsigned:
            inverted = self.evaluate(bitwise_ops.invert(input_tensor))
            expected = [dtype.max - x for x in inputs]
            self.assertAllEqual(inverted, expected)
