# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
test_value = ragged_factory_ops.constant(
    [[ord('H'), 0xC3, ord('l'), ord('l'), ord('o')],
     [ord('W'), 0x1F604, ord('r'), ord('l'), ord('d'), ord('.')]], np.int32)
expected_value = [
    u"H\xc3llo".encode(encoding), u"W\U0001f604rld.".encode(encoding)
]
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)
self.assertAllEqual(unicode_encode_op, expected_value)
