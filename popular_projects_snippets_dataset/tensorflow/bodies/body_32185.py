# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
text = constant_op.constant(u"仅今年前".encode("utf-8"))
chars = ragged_string_ops.unicode_decode(text, "utf-8")
self.assertAllEqual(chars, [ord(c) for c in u"仅今年前"])
