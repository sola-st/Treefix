# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
bom_string = b"\xfe\xff\x00\x61"  # Big-endian BOM with 'a' encoded
with self.cached_session() as sess:
    outputs = string_ops.unicode_transcode(
        bom_string, input_encoding="UTF-16-BE", output_encoding="UTF-8")
    values = self.evaluate(outputs)
    # BOM is preserved in output
    self.assertAllEqual(values, b"\xef\xbb\xbfa")

    outputs = string_ops.unicode_transcode(
        bom_string, input_encoding="UTF-16-LE", output_encoding="UTF-8")
    values = self.evaluate(outputs)
    # mangled BOM and value from (incorrect) LE encoding
    self.assertAllEqual(values, b"\xef\xbf\xbe\xe6\x84\x80")

    bom_string = b"\xff\xfe\x61\x00"  # Little-endian BOM with 'a' encoded
    outputs = string_ops.unicode_transcode(
        bom_string, input_encoding="UTF-16-LE", output_encoding="UTF-8")
    values = self.evaluate(outputs)
    self.assertAllEqual(values, b"\xef\xbb\xbfa")
