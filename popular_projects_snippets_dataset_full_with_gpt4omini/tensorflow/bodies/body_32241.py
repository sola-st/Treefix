# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_transcode_op_test.py
strings = [b"\x0e\x0e", b"\x0f\x0f"]
with self.cached_session() as sess:
    outputs = string_ops.unicode_transcode(
        strings,
        input_encoding="US-ASCII",
        output_encoding="UTF-8",
        replacement_char=ord(" "),
        replace_control_characters=False)
    values = self.evaluate(outputs)
    self.assertAllEqual(values, strings)
