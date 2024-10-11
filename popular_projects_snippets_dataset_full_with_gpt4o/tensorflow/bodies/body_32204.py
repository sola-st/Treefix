# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
text = constant_op.constant([u"仅今年前".encode("UTF-8"), b"hello"])
chars, starts = ragged_string_ops.unicode_split_with_offsets(text, "UTF-8")
expected_chars = [[c.encode("UTF-8") for c in u"仅今年前"],
                  [c.encode("UTF-8") for c in u"hello"]]
self.assertAllEqual(chars, expected_chars)
self.assertAllEqual(starts, [[0, 3, 6, 9], [0, 1, 2, 3, 4]])
