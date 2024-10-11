# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
test_value = np.array([ord('H'), ord('e'), 0x7FFFFFFF, -1, ord('o')],
                      np.int32)
expected_value = u"Heo".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding,
                                                     "ignore")
self.assertAllEqual(unicode_encode_op, expected_value)
