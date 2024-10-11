# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
strings = [
    b"\x00\x00\x00a\x00\x00\x00b\x00\x00\x20\xAC", b"\x00\x01\x04\x37"
]  # U+10437
expected = [s.decode("UTF-32-BE").encode("UTF-8") for s in strings]
with self.cached_session() as sess:
    outputs = string_ops.unicode_transcode(
        strings,
        input_encoding="UTF-32",
        output_encoding="UTF-8",
        replacement_char=ord(" "),
        replace_control_characters=False)
    values = self.evaluate(outputs)
    self.assertAllEqual(values, expected)
