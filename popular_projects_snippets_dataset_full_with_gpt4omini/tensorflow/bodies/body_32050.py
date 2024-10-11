# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
test_value = np.array([ord('H'), ord('e'), ord('l'), ord('l'), ord('o')],
                      np.int32)
expected_value = u"Hello".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)
self.assertAllEqual(unicode_encode_op, expected_value)

test_value = np.array([ord('H'), ord('e'), 0xC3, 0xC3, 0x1F604], np.int32)
expected_value = u"He\xc3\xc3\U0001f604".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)
self.assertAllEqual(unicode_encode_op, expected_value)

# Single character string
test_value = np.array([ord('H')], np.int32)
expected_value = u"H".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)
self.assertAllEqual(unicode_encode_op, expected_value)

test_value = np.array([0x1F604], np.int32)
expected_value = u"\U0001f604".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)
self.assertAllEqual(unicode_encode_op, expected_value)
