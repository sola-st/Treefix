# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
test_value = np.array(
    [[72, 0x1F604, 108, 108, 111], [87, 0x1F604, 114, 108, 100]], np.int32)
expected_value = [
    u"H\U0001f604llo".encode(encoding), u"W\U0001f604rld".encode(encoding)
]
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)
self.assertAllEqual(unicode_encode_op, expected_value)
