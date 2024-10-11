# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
bom_string = b"\xef\xbb\xbfabcdefg"
with self.cached_session() as sess:
    outputs = string_ops.unicode_transcode(
        bom_string, input_encoding="UTF-8", output_encoding="UTF-8")
    values = self.evaluate(outputs)
    self.assertAllEqual(values, b"\xef\xbb\xbfabcdefg")  # BOM preserved

    outputs = string_ops.unicode_transcode(
        bom_string, input_encoding="UTF-8", output_encoding="UTF-16-BE")
    values = self.evaluate(outputs)
    utf16expected = bom_string.decode("UTF-8").encode("UTF-16-BE")
    self.assertAllEqual(values, utf16expected)
