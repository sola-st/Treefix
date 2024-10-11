# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
test_value = ragged_factory_ops.constant(
    [[[72, 101, 108, 108, 111], [87, 111, 114, 108, 100, 46]],
     [[68, 111, 110, 39, 116], [119, 195, 114, 114, 121, 44, 32, 98, 101]],
     [[0x1F604], []]], np.int32)
expected_value = [[u"Hello".encode(encoding), u"World.".encode(encoding)],
                  [
                      u"Don't".encode(encoding),
                      u"w\xc3rry, be".encode(encoding)
                  ], [u"\U0001f604".encode(encoding), u"".encode(encoding)]]
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)
self.assertAllEqual(unicode_encode_op, expected_value)
