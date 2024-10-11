# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
text = constant_op.constant([u"仅今年前".encode("utf-8"), b"hello"])
chars = ragged_string_ops.unicode_decode(text, "utf-8")
expected_chars = [[ord(c) for c in u"仅今年前"],
                  [ord(c) for c in u"hello"]]
self.assertAllEqual(chars, expected_chars)
