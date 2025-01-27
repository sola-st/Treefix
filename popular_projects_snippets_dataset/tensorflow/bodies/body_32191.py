# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
texts = [s.encode("utf8") for s in [u"G\xf6\xf6dnight", u"\U0001f60a"]]
codepoints1 = ragged_string_ops.unicode_decode(texts, "UTF-8")
codepoints2, offsets = ragged_string_ops.unicode_decode_with_offsets(
    texts, "UTF-8")
self.assertAllEqual(
    codepoints1, [[71, 246, 246, 100, 110, 105, 103, 104, 116], [128522]])
self.assertAllEqual(
    codepoints2, [[71, 246, 246, 100, 110, 105, 103, 104, 116], [128522]])
self.assertAllEqual(offsets, [[0, 1, 3, 5, 6, 7, 8, 9, 10], [0]])
