# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
test_value = np.array([ord('H'), ord('e'), 0x7FFFFFFF, -1, ord('o')],
                      np.int32)
expected_value = u"He\U0000fffd\U0000fffdo".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding,
                                                     "replace")
self.assertAllEqual(unicode_encode_op, expected_value)

# Test custom replacement character
test_value = np.array([ord('H'), ord('e'), 0x7FFFFFFF, -1, ord('o')],
                      np.int32)
expected_value = u"Heooo".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding,
                                                     "replace", ord('o'))
self.assertAllEqual(unicode_encode_op, expected_value)

# Verify "replace" is default
test_value = np.array([ord('H'), ord('e'), 0x7FFFFFFF, -1, ord('o')],
                      np.int32)
expected_value = u"He\U0000fffd\U0000fffdo".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)
self.assertAllEqual(unicode_encode_op, expected_value)

# Verify non-default replacement with an unpaired surrogate.
test_value = np.array([0xD801], np.int32)
expected_value = u"A".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding,
                                                     "replace", 0x41)
self.assertAllEqual(unicode_encode_op, expected_value)

# Test with a noncharacter code point.
test_value = np.array([0x1FFFF], np.int32)
expected_value = u"A".encode(encoding)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding,
                                                     "replace", 0x41)
self.assertAllEqual(unicode_encode_op, expected_value)

# Replacement_char must be within range
test_value = np.array([ord('H'), ord('e'), 0x7FFFFFFF, -1, ord('o')],
                      np.int32)
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding,
                                                     "replace", 0x110000)
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(unicode_encode_op)
