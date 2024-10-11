# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/binary_ops_test.py
for dtype in self.signed_int_types:
    self._testBinary(
        gen_math_ops.truncate_div,
        np.array([3, 3, -1, -9, -8], dtype=dtype),
        np.array([2, -2, 7, 2, -4], dtype=dtype),
        expected=np.array([1, -1, 0, -4, 2], dtype=dtype))
    self._testSymmetricBinary(
        bitwise_ops.bitwise_and,
        np.array([0b1, 0b101, 0b1000], dtype=dtype),
        np.array([0b0, 0b101, 0b1001], dtype=dtype),
        expected=np.array([0b0, 0b101, 0b1000], dtype=dtype))
    self._testSymmetricBinary(
        bitwise_ops.bitwise_or,
        np.array([0b1, 0b101, 0b1000], dtype=dtype),
        np.array([0b0, 0b101, 0b1001], dtype=dtype),
        expected=np.array([0b1, 0b101, 0b1001], dtype=dtype))
    self._testSymmetricBinary(
        bitwise_ops.bitwise_xor,
        np.array([0b1, 0b111, 0b1100], dtype=dtype),
        np.array([0b0, 0b101, 0b1001], dtype=dtype),
        expected=np.array([0b1, 0b010, 0b0101], dtype=dtype))

    lhs = np.array([0, 5, 3, 14], dtype=dtype)
    rhs = np.array([5, 0, 7, 11], dtype=dtype)
    self._testBinary(
        bitwise_ops.left_shift, lhs, rhs, expected=np.left_shift(lhs, rhs))
    self._testBinary(
        bitwise_ops.right_shift, lhs, rhs, expected=np.right_shift(lhs, rhs))

    if dtype in [np.int8, np.int16, np.int32, np.int64]:
        lhs = np.array([-1, -5, -3, -14, -2], dtype=dtype)
        rhs = np.array([5, 0, 1, 11, 36], dtype=dtype)
        # HLO has saturating shift behavior.
        bits = np.ceil(
            np.log(np.iinfo(dtype).max - np.iinfo(dtype).min) / np.log(2))
        expected = [
            np.right_shift(l, r) if r < bits else np.sign(l)
            for l, r in zip(lhs, rhs)
        ]
        self._testBinary(bitwise_ops.right_shift, lhs, rhs, expected=expected)
