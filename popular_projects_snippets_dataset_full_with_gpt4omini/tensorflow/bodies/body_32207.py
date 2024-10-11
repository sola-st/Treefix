# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_decode_op_test.py
texts = [s.encode("utf8") for s in [u"G\xf6\xf6dnight", u"\U0001f60a"]]
codepoints1 = ragged_string_ops.unicode_split(texts, "UTF-8")
codepoints2, offsets = ragged_string_ops.unicode_split_with_offsets(
    texts, "UTF-8")
self.assertAllEqual(
    codepoints1,
    [[b"G", b"\xc3\xb6", b"\xc3\xb6", b"d", b"n", b"i", b"g", b"h", b"t"],
     [b"\xf0\x9f\x98\x8a"]])
self.assertAllEqual(
    codepoints2,
    [[b"G", b"\xc3\xb6", b"\xc3\xb6", b"d", b"n", b"i", b"g", b"h", b"t"],
     [b"\xf0\x9f\x98\x8a"]])
self.assertAllEqual(offsets, [[0, 1, 3, 5, 6, 7, 8, 9, 10], [0]])
