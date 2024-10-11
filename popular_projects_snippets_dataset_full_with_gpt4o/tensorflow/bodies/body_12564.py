# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/bitwise_ops_test.py
dtype_list = [np.int8, np.int16, np.int32, np.int64]

with self.session() as sess:
    for dtype in dtype_list:
        lhs = np.array([-1, -5, -3, -14], dtype=dtype)
        rhs = np.array([-2, 64, 101, 32], dtype=dtype)
        # We intentionally do not test for specific values here since the exact
        # outputs are implementation-defined. However, we should not crash or
        # trigger an undefined-behavior error from tools such as
        # AddressSanitizer.
        sess.run([bitwise_ops.left_shift(lhs, rhs),
                  bitwise_ops.right_shift(lhs, rhs)])
