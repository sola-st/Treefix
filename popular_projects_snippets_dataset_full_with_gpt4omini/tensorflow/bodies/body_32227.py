# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
strings = [b"\x00a\x00b\x20\xAC", b"\xD8\x01\xDC\x37"]  # U+10437
expected = [s.decode("UTF-16-BE").encode("UTF-8") for s in strings]

with self.cached_session() as sess:
    outputs = string_ops.unicode_transcode(
        strings,
        input_encoding="UTF-16",
        output_encoding="UTF-8",
        errors="replace",
        replacement_char=ord(" "),
        replace_control_characters=False)
    values = self.evaluate(outputs)
    self.assertAllEqual(values, expected)
