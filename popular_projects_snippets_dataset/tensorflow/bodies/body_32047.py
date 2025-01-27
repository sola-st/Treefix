# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
test_value = np.array([ord('H'), ord('e'), 0x7FFFFFFF, -1, ord('o')],
                      np.int32)
with self.cached_session() as session:
    with self.assertRaises(errors.InvalidArgumentError):
        session.run(
            ragged_string_ops.unicode_encode(test_value, encoding, "strict"))
